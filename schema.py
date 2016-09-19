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
__date__   =  "2016-09-18"

import graphene

class Book(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    price = graphene.Int()
    is_rent = graphene.Boolean()
    is_sold = graphene.Boolean()

class Stock(graphene.ObjectType):
    id = graphene.ID()
    count = graphene.Int()
    books = graphene.List(Book)

class SearchQuery(graphene.InputObjectType):
    id = graphene.ID(required=False)
    name = graphene.String(required=False)

class Arrival(graphene.Mutation):
    success = graphene.Boolean()
    reason = graphene.String()
    book = graphene.Field(Book)

    @staticmethod
    def mutate(cls, args, context, info):
        print args.get('title')
        print args.get('description')
        print args.get('price')
        return Arrival(success=True, reason="", book=Book())

    class Input:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        price = graphene.Int(required=True)

class Sold(graphene.Mutation):
    success = graphene.Boolean()
    reason = graphene.String()
    book = graphene.Field(Book)

    @staticmethod
    def mutate(cls, args, context, info):
        print args.get('id')
        return Sold(success=True, reason="", book=Book())

    class Input:
        id = graphene.ID(required=True)

class Rent(graphene.Mutation):
    success = graphene.Boolean()
    reason = graphene.String()
    book = graphene.Field(Book)

    @staticmethod
    def mutate(cls, args, context, info):
        print args.get('id')
        return Rent(success=True, reason="", book=Book())

    class Input:
        id = graphene.ID(required=True)

class Query(graphene.ObjectType):
    stock = graphene.Field(Stock, search=SearchQuery())

    def resolve_stock(self, args, context, info):
        uid = 0
        s = args.get('search')
        if s and s['id']:
            uid = s['id']
        return Stock(id=uid, count=0, books=[])

class Mutation(graphene.ObjectType):
    arrival = Arrival.Field()
    sold = Sold.Field()
    rent = Rent.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
