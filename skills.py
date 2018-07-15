#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

import json
import sys
import os
import requests
from dueros.Bot import Bot

from dueros.directive.Display.RenderTemplate import RenderTemplate
from dueros.directive.Display.template.BodyTemplate1 import BodyTemplate1

from dueros.card.ImageCard import ImageCard
from dueros.card.ListCard import ListCard
from dueros.card.ListCardItem import ListCardItem
from dueros.card.StandardCard import StandardCard
from dueros.card.TextCard import TextCard

class LifeSkill(Bot):

    def __init__(self, data):

        super().__init__(data)
        self.data = data
        self.addLaunchHandler(self.launchRequest)
        self.addIntentHandler('welcome', self.welcome)
        self.addIntentHandler('outside_skill', self.outside_skill)
        self.addIntentHandler('useful_skill', self.useful_skill)
        self.addIntentHandler('home_skill', self.home_skill)
        self.addIntentHandler('kid_skill', self.kid_skill)
        self.addIntentHandler('ai.dueros.common.default_intent', self.quesheng)
        self.usefulbackGroundImage = 'http://dbp-resource.gz.bcebos.com/75acb57c-152f-c3bf-24f2-4e6b5ae01002/2.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-14T10%3A49%3A07Z%2F-1%2F%2F34070ce31d2b6e606fe0e60387ed6e2d00f95cd83d89d23cb13d7ba1c5920e71'
        self.lifebackGroundImage = 'http://dbp-resource.gz.bcebos.com/75acb57c-152f-c3bf-24f2-4e6b5ae01002/3.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-14T10%3A49%3A07Z%2F-1%2F%2F6df52e2ba585c64799f6d9af419d743837dcf2339592dffae37667ada0dd6345'
        self.kidbackGroundImage = 'http://dbp-resource.gz.bcebos.com/75acb57c-152f-c3bf-24f2-4e6b5ae01002/1.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-14T10%3A49%3A02Z%2F-1%2F%2Faacb8528116d26c2de3f5ea0e1b01b6e7b489d4ff0586f3fc9366dad1bbb8fa6'
        self.home_ask = {
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': ''
        }
        self.kid_ask = {
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': ''
        }
        self.useful_ask = {
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': ''
        }
        self.outside_ask = {
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': '',
            '': ''
        }

    def launchRequest(self):

        """
        进入
        :return:


        """
        bodyTemplate = BodyTemplate1()
        bodyTemplate.setBackGroundImage(self.lifebackGroundImage)
        bodyTemplate.setPlainTextContent(r'欢迎使用生活小技巧！在这里，您可以了解到关于旅游、实用、居家、照顾婴儿等小技巧。试着对我说“居家小技巧”')

        directive = RenderTemplate(bodyTemplate)
        return {
            'directives': [directive],
            'outputSpeech': r'欢迎使用生活小技巧！在这里，您可以了解到关于外l旅游、实用、居家、照顾婴儿等小技巧。试着对我说，居家小技巧，'
        }

    def outside_skill(self):

        """
        外出小技巧
        :return: 
        """
        ask = getSlots('trip_dict')
        if not ask:
            self.nlu.ask('ask')
            card = StandardCard()
            card.setContent(r'请问您想了解些什么旅游小技巧呢？试着对我问一些问题')
            return {
                'card': card,
                'outputSpeech': r'请问您想了解些什么旅游小技巧呢？试着对我问一些问题'
            }
        else:
            try:
                answer = self.outside_ask['ask']
            except KeyError:
                return {
                    'outputSpeech': r'对不起，我还不知道呢'
                }
            else:
                bodyTemplate = BodyTemplate1()
                bodyTemplate.setBackGroundImage(self.lifebackGroundImage)
                bodyTemplate.setPlainTextContent(answer)
                bodyTemplate.setTitle(ask)
                directive = RenderTemplate(bodyTemplate)
                return {
                    'directives': [directive],
                    'outputSpeech': answer
                }

    def useful_skill(self):

        """
        实用小技巧
        :return:
        """
        """
        外出小技巧
        :return: 
        """
        ask = getSlots('trip_dict')
        if not ask:
            self.nlu.ask('ask')
            card = StandardCard()
            card.setContent(r'请问您想了解些什么实用的小技巧呢？试着对我问一些问题')
            return {
                'card': card,
                'outputSpeech': r'请问您想了解些什么实用的小技巧呢？试着对我问一些问题'
            }
        else:
            try:
                answer = self.useful_ask['ask']
            except KeyError:
                return {
                    'outputSpeech': r'对不起，我还不知道呢'
                }
            else:
                bodyTemplate = BodyTemplate1()
                bodyTemplate.setBackGroundImage(self.usefulbackGroundImage)
                bodyTemplate.setPlainTextContent(answer)
                bodyTemplate.setTitle(ask)
                directive = RenderTemplate(bodyTemplate)
                return {
                    'directives': [directive],
                    'outputSpeech': answer
                }

    def home_skill(self):

        """
        居家小技巧
        :return:
        """
        """
        外出小技巧
        :return: 
        """
        ask = getSlots('home_dict')
        if not ask:
            self.nlu.ask('ask')
            card = StandardCard()
            card.setContent(r'请问您想了解些什么居家的小技巧呢？试着对我问一些问题')
            return {
                'card': card,
                'outputSpeech': r'请问您想了解些什么居家的小技巧呢？试着对我问一些问题'
            }
        else:
            try:
                answer = self.outside_ask['ask']
            except KeyError:
                return {
                    'outputSpeech': r'对不起，我还不知道呢'
                }
            else:
                bodyTemplate = BodyTemplate1()
                bodyTemplate.setBackGroundImage(self.lifebackGroundImage)
                bodyTemplate.setPlainTextContent(answer)
                bodyTemplate.setTitle(ask)
                directive = RenderTemplate(bodyTemplate)
                return {
                    'directives': [directive],
                    'outputSpeech': answer
                }

    def kid_skill(self):

        """
        照顾婴儿小技巧
        :return:
        """
        """
        外出小技巧
        :return: 
        """
        ask = getSlots('kid_dict')
        if not ask:
            self.nlu.ask('ask')
            card = StandardCard()
            card.setContent(r'请问您想了解些什么照顾婴儿小技巧呢？试着对我问一些问题')
            return {
                'card': card,
                'outputSpeech': r'请问您想了解些什么照顾婴儿小技巧呢？试着对我问一些问题'
            }
        else:
            try:
                answer = self.kid_ask['ask']
            except KeyError:
                return {
                    'outputSpeech': r'对不起，我还不知道呢'
                }
            else:
                bodyTemplate = BodyTemplate1()
                bodyTemplate.setBackGroundImage(self.kidbackGroundImage)
                bodyTemplate.setPlainTextContent(answer)
                bodyTemplate.setTitle(ask)
                directive = RenderTemplate(bodyTemplate)
                return {
                    'directives': [directive],
                    'outputSpeech': answer
                }

    def welcome(self):

        """
        使用介绍
        :return:
        """
        pass
