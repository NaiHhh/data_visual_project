$ = layui.jquery;

function get_anime_top() {
    $.ajax({
    //几个参数需要注意一下
        type: "POST",//方法类型
        contentType: "application/json;charset=utf-8",
        url: "http://127.0.0.1:5000/anime" ,//url
        success: function (result) {
            result = JSON.parse(result);
            if(result.code===200){
                anime_top(result.data)
            }else{
                alert("请输入正确的cid");
            }
        }
    });
}

get_anime_top()
  // 通过后端获取数据

  // 基于准备好的dom，初始化echarts实例
function anime_top(result){

    var chartDom = document.getElementById('anime_top');
    var myChart = echarts.init(chartDom);
    var option;

    option = {
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'cross',
          crossStyle: {
            color: '#999'
          }
        }
      },
      toolbox: {
        feature: {
          dataView: { show: true, readOnly: false },
          magicType: { show: true, type: ['line', 'bar'] },
          restore: { show: true },
          saveAsImage: { show: true }
        }
      },
      legend: {
        data: ['追番人数', '弹幕量', '综合评分']
      },
      xAxis: [
        {
          type: 'category',
          data: result[0],
          axisPointer: {
            type: 'shadow'
          },
          axisLabel: {
            rotate: 40
          }
        }
      ],
      yAxis: [
        {
          type: 'value',
          name: '弹幕量',
          min: 0,
          max: 11000000,
          interval: 800000,
          axisLabel: {
            formatter: '{value}'
          }
        },
        {
          type: 'value',
          name: '综合评分',
          min: 0,
          max: 10,
          interval: 2,
          axisLabel: {
            formatter: '{value} '
          }
        }
      ],
      series: [
        {
          name: '追番人数',
          type: 'bar',
          tooltip: {
            valueFormatter: function (value) {
              return value;
            }
          },
          data: result[1]
        },
        {
          name: '弹幕量',
          type: 'bar',
          tooltip: {
            valueFormatter: function (value) {
              return value;
            }
          },
          data: result[2]
        },
        {
          name: '综合评分',
          type: 'line',
          yAxisIndex: 1,
          tooltip: {
            valueFormatter: function (value) {
              return value;
            }
          },
          data: result[3]
        }
      ],
      dataZoom: [
          {
            type: "slider",
            show: true,
            start: 0,
            end: 30,
            xAxisIndex: [0],
          }
      ],
    };

    option && myChart.setOption(option);

}
