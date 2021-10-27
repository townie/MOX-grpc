#
# Copyright 2018 Vizor Games LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.See the
# License for the specific language governing permissions and limitations
# under the License.
#
import os

from colorama import Fore
from subprocess import Popen, PIPE
from src.util import Misc, PathConverter
from src.config import Config


class ProtoTask:
    def __init__(self, lang: str, out_dir: str, proto_file: str):
        """
        Runs protoc to generate wrapper for proto_file
        :param lang: language from list of available languages
        :param out_dir: an ABSOLUTE path to the directory where generated code will reside
        :param proto_file: a RELATIVE (to self.grpc_root) path to .proto file
        """
        self.lang = lang
        self.out_dir = out_dir
        self.proto_file = proto_file

    def run(self, config: Config, proto_root: str):
        abs_proto_file = PathConverter.to_absolute(proto_root, self.proto_file)

        if not os.path.exists(abs_proto_file):
            raise SystemError(f"{self.proto_file} does not exist in {proto_root}")

        programs_root = os.path.abspath(os.path.join(config['programs_root'], Misc.get_binary_release_os()))

        if not programs_root:
            raise Exception("programs_root config variable should be defined")

        if not os.path.isdir(programs_root):
            raise Exception(f"programs_root: {programs_root} is not a directory")

        include_dir = proto_root + PathConverter.include_suffix(self.proto_file)
        path_to_proto_compiler = f"{os.path.join(programs_root, Misc.add_exec_suffix('protoc'))}"

        gen_transport = config['transport']
        options = [path_to_proto_compiler, f'--proto_path={include_dir}']

        path_to_plugin = os.path.join(programs_root, Misc.add_exec_suffix(Misc.plugin_for_lang(self.lang)))

        if 'protoc_options' in config.options.keys():
            for opt in self.getOptions(config["protoc_options"]):
                options.append(opt)

        if self.lang == 'go':
            if 'protoc_options_go' in config.options.keys():
                for opt in self.getOptions(config["protoc_options_go"]):
                    options.append(opt)

            options.append(f'--plugin={path_to_plugin}')

            if gen_transport:
                options.append(f'--{self.lang}_out=plugins=grpc:{self.out_dir}')
            else:
                options.append(f'--{self.lang}_out={self.out_dir}')
        else:
            options.append(f'--{self.lang}_out={self.out_dir}')

        # if we're generating transport code, we must declare a plugin and --grpc_out
        if gen_transport and (self.lang != 'go'):
            options += [
                f'--plugin=protoc-gen-grpc={path_to_plugin}',
                f'--grpc_out={self.out_dir}'
            ]

        # finally add the file to generate wrapper to
        options.append(abs_proto_file)

        if config['verbose']:
            print(Fore.MAGENTA + f">> {' '.join(options)}")

        p = Popen(options, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()

        if p.returncode != 0:
            if config['porcelain']:
                raise SyntaxError('Unable to convert {} to {}. Error: {}'.format(
                    self.proto_file,
                    Misc.pretty_language_name(self.lang),
                    err.decode('utf-8')
                ))
            else:
                raise SyntaxError('Unable to convert {} to {}\nInvocation: {}\nReturn code: {}, error: {}'.format(
                    self.proto_file,
                    Misc.pretty_language_name(self.lang),
                    ' '.join(options),
                    p.returncode,
                    err.decode('utf-8')
                ))

    def getOptions(self, options: dict):
        result = []
        for opt in options:
            if type(opt) != str:
                continue

            if '@out_dir' in opt:
                opt = opt.replace("@out_dir", f"{self.out_dir}")
            result.append(os.path.expandvars(opt))

        return result
