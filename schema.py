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
import data_manager as manager
from model import Book, Stock, SearchQuery, IResult

class Arrival(graphene.Mutation):
    @staticmethod
    def mutate(cls, args, context, info):
        return manager.arrival(args).to_model(Arrival)

    class Meta:
        interfaces = (IResult, )

    class Input:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        price = graphene.Int(required=True)

class Sold(graphene.Mutation):
    @staticmethod
    def mutate(cls, args, context, info):
        return manager.sold(args.get('id')).to_model(Sold)

    class Meta:
        interfaces = (IResult, )

    class Input:
        id = graphene.ID(required=True)

class Rent(graphene.Mutation):
    @staticmethod
    def mutate(cls, args, context, info):
        return manager.rent(args.get('id')).to_model(Rent)

    class Meta:
        interfaces = (IResult, )

    class Input:
        id = graphene.ID(required=True)

class Query(graphene.ObjectType):
    stock = graphene.Field(Stock, search=SearchQuery())

    def resolve_stock(self, args, context, info):
        uid = 0
        s = args.get('search')
        if s and s['id']:
            uid = s['id']
        return manager.stock(args)

class Mutation(graphene.ObjectType):
    arrival = Arrival.Field()
    sold = Sold.Field()
    rent = Rent.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
