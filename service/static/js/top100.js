$ = layui.jquery;

function top100_play() {
    $.ajax({
    //几个参数需要注意一下
        type: "POST",//方法类型
        contentType: "application/json;charset=utf-8",
        url: "http://127.0.0.1:5000/get_play_list" ,//url
        // data: '{"cid":"' + cid + '"}',
        success: function (result) {
            result = JSON.parse(result);
            if(result.code===200){
                get_top_100_play(result.data)
            }else{
                alert("请输入正确的cid");
            }
        }
    });
}

top100_play()
  // 通过后端获取数据

  // 基于准备好的dom，初始化echarts实例
function get_top_100_play(result){
  var chartDom = document.getElementById('play_list');
  var myChart = echarts.init(chartDom);
  var option;

  option = {
    title: {
      text: '播放量排行榜前十',
      subtext: '',
      left: 'center'
    },
    tooltip: {
      trigger: 'item'
    },
    legend: {
      orient: 'vertical',
      left: 'left'
    },
    series: [
      {
        name: 'Access From',
        type: 'pie',
        radius: '50%',
        data: result,
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  };

  option && myChart.setOption(option);
}

