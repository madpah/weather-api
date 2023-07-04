# encoding: utf-8

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) Paul Horton. All Rights Reserved.

import weather
from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/local/temp/now')
def current_temperature_now():
    forecast = weather.forecast().today
    current_hour = f'{datetime.now().hour}:00'

    return {
        "temp": forecast[current_hour].temp
    }


@app.route('/version')
def version():
    return {
        "name": __name__,
        "version": 'tbc'
    }
