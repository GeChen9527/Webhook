#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json, channel.Dingtalk, channel.mail

def grafana_alarm(json_data,channel_data):
    alarm_status = json_data["state"]
    if alarm_status == "alerting":
        grafana_value = json_data["evalMatches"]
        alarm_value = grafana_value[0]["value"]
        alarm_metric = grafana_value[0]["metric"]
        alarm_image = json_data["imageUrl"]
        alarm_name = json_data["title"]
        alarm_url = json_data["ruleUrl"]
        alarm_status = json_data["state"]
    else:
        alarm_image = json_data["imageUrl"]
        alarm_name = json_data["title"]
        alarm_url = json_data["ruleUrl"]
        alarm_status = json_data["state"]

    channel_data_list = json.loads(channel_data)
    for index in range(len(channel_data_list)):
        if channel_data_list[index] == 1:
            if alarm_status == "alerting":
                Ding = channel.Dingtalk.Dingtalk_alerting(alarm_value, alarm_metric, alarm_image, alarm_name, alarm_url, alarm_status)
            else:
                Ding = channel.Dingtalk.Dingtalk_ok(alarm_image, alarm_name, alarm_url, alarm_status)
            return Ding
        elif channel_data_list[index] == 2:
            Ding = channel.mail
            return Ding
        else:
            return "Not Found alarm channel!"

    return "1"