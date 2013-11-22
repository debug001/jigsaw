#encoding=utf-8
from base import Base
from error import EchartsException
#encoding=utf-8
from base import Base
from error import EchartsException
import sys, re, types
reload(sys)
sys.setdefaultencoding('utf-8')


class Map(Base):

    def __init__(self, **configs):
        super(Base, self).__init__()
        self.configs = configs

    def get_seriesname(self, data):
        result = []
        for row in data:
            if type(row[1]) is types.StringType:
                result.append(row[0])
            else:
                result.append('None')
        return result

    def data_hashmap(self, data):
        result = "["
        flag = 1

        if type(data[1]) is types.StringType:
            data = data[1:]

        s = ""
        for index in data:
            if flag % 2:
                s += "{{name: '{name}', ".format(name=index)
            else:
                s += "value: {value}}},".format(value=index)
            result += s
            s = ""
            flag += 1

        result += "]"
        return result

    def get_max(self, data):
        max = 0
        for row in data:
            for n in row:
                if type(n) is types.IntType:
                    if n > max:
                        max = n

        return max
    
    


    def create(self):
        rows = eval(self.configs['data'])
        print rows
        
        series_name = self.get_seriesname(rows['data'])
        series_data = self.convert_list(series_name)
        max = self.get_max(rows['data'])


        js = r"""
        <script>
            require.config({{
                packages: [
                    {{
                        name: 'echarts',
                        location: '/echarts/src',      
                        main: 'echarts'
                    }},
                    {{
                        name: 'zrender',
                        location: '/zrender/src', 
                        main: 'zrender'
                    }}
                ]
            }});

             require(
                    [
                        'echarts',
                        'echarts/chart/map'
                    ],
                    function(ec) {{
                        var myChart = ec.init(document.getElementById('{id}')); 
                        var option = {{
                        title : {{
                            text: '{title}',
                            x:'center'
                        }},
                        tooltip : {{
                            trigger: 'item'
                        }},
                        legend: {{
                            orient: 'vertical',
                            x:'left',
                            data: {series_data}
                        }},
                        dataRange: {{
                            min: 0,
                            max: {max},
                            text:['高','低'],           
                            calculable : true,
                            textStyle: {{
                                color: 'orange'
                            }}
                        }},
                        toolbox: {{
                            show : true,
                            orient : 'vertical',
                            x: 'right',
                            y: 'center',
                            feature : {{
                                mark : true,
                                dataView : {{readOnly: false}},
                                restore : true,
                                saveAsImage : true
                            }}
                        }},
                        series : [
        """.format(
            id = self.configs['id'],
            title = rows['title'],
            series_data = series_data,
            max = (max+100)/100*100
        )


        for index in range(len(series_name)):
            js += """
                        {{
                             name:'{sname}',
                             type: 'map',
                                    mapType: 'china',
                                    itemStyle:{{
                                        normal:{{label:{{show:true}}}},
                                        emphasis:{{label:{{show:true}}}}
                                    }},
                                    data: {data}
                        }},
                             
            """.format(
                sname = series_name[index],
                data = self.data_hashmap(rows['data'][index])
            )

        js += """
                ]
            };
                        myChart.setOption(option);

                        }
                       );
        </script>
        """









        


        print js
        js = js.replace('"', '\"')
        js = js.replace("\n", "")
        return js 

        #return "map test"

      
