


$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];
    var ChartList = [];

    function new_card(content) {
        var listview = document.getElementById("listview");

        var card = document.createElement("DIV");
        card.className = "card";
        var card_body = document.createElement("DIV");
        card_body.className = "card-body";


        card_body.appendChild(content);
        card.appendChild(card_body);

        // appending button to div
        listview.appendChild(card);
    }


    //receive details from server
    socket.on('server', function(data) {
          console.log("hej");
            var config;
            var ctx;
            if(document.getElementById(data.id)){

            ChartList.forEach(function(chart){
          //      console.log(chart);
                if(chart.config.id == data.id){
                  config = chart.config;
                  ctx = chart;
                }
              });
              if( config == null || ctx == null){
                return;
              }


              if (config.data.labels.length === 200) {
                  config.data.labels.shift();
                  config.data.datasets[0].data.shift();
              }
              config.data.labels.push(data.time);
              config.data.datasets[0].data.push(data.value);
              ctx.update();

            } else {
              // Create graph

              var canvas = document.createElement('CANVAS');

              canvas.id = data.id;

              var config = {
                  type: 'line',
                  id: data.id,
                  data: {
                      labels: [],
                      datasets: [{
                          label: "Random Dataset",
                          backgroundColor: 'rgb(255, 99, 132)',
                          borderColor: 'rgb(255, 99, 132)',
                          data: [],
                          fill: false,
                      }],
                  },
                  options: {
                      responsive: true,
                      title: {
                          display: true,
                          text: 'Creating Real-Time Charts with Flask'
                      },
                      tooltips: {
                          mode: 'index',
                          intersect: false,
                      },
                      hover: {
                          mode: 'nearest',
                          intersect: true
                      },
                      scales: {
                          xAxes: [{
                              display: true,
                              scaleLabel: {
                                  display: true,
                                  labelString: 'Time'
                              }
                          }],
                          yAxes: [{
                              display: true,
                              scaleLabel: {
                                  display: true,
                                  labelString: 'Value'
                              }
                          }]
                      }
                  }
              };


              var lineChart = new Chart(canvas, config);
            //  lineChart.id = data.id+"chart";

            ChartList.push(lineChart);
            console.log(lineChart);
            console.log(canvas);
              new_card(canvas);

          //    var v = $( "#listview" ).append(lineChart);
            //  console.log(v);

            }
        }

        //maintain a list of ten numbers
        if (numbers_received.length >= 10){
            numbers_received.shift()
        }
        numbers_received.push(msg.number);
        numbers_string = '';
        for (var i = 0; i < numbers_received.length; i++){
            numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>';
        }
        $('#log').html(numbers_string);
    });

});
