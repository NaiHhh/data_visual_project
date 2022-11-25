$ = layui.jquery;

function fans_top() {
    $.ajax({
    //几个参数需要注意一下
        type: "POST",//方法类型
        contentType: "application/json;charset=utf-8",
        url: "http://127.0.0.1:5000/fans_top" ,//url
        // data: '{"cid":"' + cid + '"}',
        success: function (result) {
            result = JSON.parse(result);
            if(result.code===200){
                fans_top_function(result.data)
            }else{
                alert("请输入正确的cid");
            }
        }
    });
}

fans_top()

function fans_top_function(result){
    var chartDom = document.getElementById('fans_top');
    var myChart = echarts.init(chartDom);
    var option;

    option = {
      xAxis: {
        type: 'category',
        data: result[0],
        axisLabel: {
            rotate: 40
        }
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          data: result[1],
          type: 'bar'
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
