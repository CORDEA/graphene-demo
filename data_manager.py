#!/usr/bin/env python
# encoding:utf-8
#
# Copyright 2016 Yoshihiro Tanaka
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__Author__ =  "Yoshihiro Tanaka <contact@cordea.jp>"
__date__   =  "2016-09-20"

import os, json, glob
from model import Book, Stock, Result

dirname = 'books/'

def __create_dir():
    if not os.path.exists(dirname):
        os.mkdir(dirname)

def __dict_to_book(dic):
    book = Book()
    for k, v in dic.items():
        setattr(book, k, v)
    return book

def arrival(args):
    if not os.path.exists(dirname):
        return
    indexes = [int(r.split('/')[1].split('.json')[0]) for r in glob.glob(dirname + '*.json')]
    index = (0 if len(indexes) == 0 else max(indexes)) + 1
    book = Book(index, args.get('title'), args.get('description'), args.get('price'), False, False)
    j = json.dumps(book.__dict__, sort_keys=True, indent=4)
    with open(dirname + str(index) + '.json', 'w') as f:
        f.write(j)
    return Result(True, "", book)

def rent(id):
    if not os.path.exists(dirname):
        return
    name = id + '.json'
    with open(dirname + name, 'r+') as f:
        j = json.loads(f.read())
        f.truncate(0)
        j['is_rent'] = True
        f.write(json.dumps(j, sort_keys=True, indent=4))
        return Result(True, "", __dict_to_book(j))
    return Result(False, "", None)

def sold(id):
    if not os.path.exists(dirname):
        return
    name = id + '.json'
    with open(dirname + name, 'r+') as f:
        j = json.loads(f.read())
        f.truncate(0)
        j['is_sold'] = True
        f.write(json.dumps(j, sort_keys=True, indent=4))
        return Result(True, "", __dict_to_book(j))
    return Result(False, "", None)

def __find_by_id(id, filename):
    if id + '.json' == name:
        with open(name) as f:
            j = json.loads(f.read())
            return __dict_to_book(j)

def __find_by_title(title, filename):
    with open(name) as f:
        j = json.loads(f.read())
        if name in j['title']:
            return __dict_to_book(j)

def stock(query):
    __create_dir()
    id = query.get('id')
    title = query.get('name')

    results = []
    for filename in glob.glob(dirname + '*.json'):

        if title and id:
            result = __find_by_id(id, filename)
            if result:
                result = __find_by_title(title, filename)
            if result:
                results.append(result)
            return

        if title:
            result = __find_by_title(title, filename)
            if result:
                results.append(result)
            return

        if id:
            result = __find_by_id(id, filename)
            if result:
                results.append(result)
            return

        with open(filename) as f:
            j = json.loads(f.read())
            results.append(__dict_to_book(j))

    return Stock(0, len(results), results)
