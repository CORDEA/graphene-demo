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

import graphene

class IBook(graphene.Interface):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    price = graphene.Int()
    is_rent = graphene.Boolean()
    is_sold = graphene.Boolean()

class Book(graphene.ObjectType):
    class Meta:
        interfaces = (IBook, )
    pass

class IStock(graphene.Interface):
    id = graphene.ID()
    count = graphene.Int()
    books = graphene.List(Book)

class Stock(graphene.ObjectType):
    class Meta:
        interfaces = (IStock, )
    pass

class IResult(graphene.Interface):
    success = graphene.Boolean()
    reason = graphene.String()
    book = graphene.Field(Book)

class Result(graphene.ObjectType):
    class Meta:
        interfaces = (IResult, )

    def to_model(self, model):
        m = model()
        for k, v in self.__dict__.items():
            setattr(m, k, v)
        return m

class SearchQuery(graphene.InputObjectType):
    id = graphene.ID(required=False)
    name = graphene.String(required=False)


