var app = angular.module("chartApp", []);
 
app.controller("DonutChartController", ["$scope", function($scope) {
  $scope.green = 50;
  $scope.red = 50;

  $scope.isValidPercent = function(val) {
    if (isNaN(val)) { return false; }
    if (val < 0) { return false; }
    if (val > 100) { return false; }
    return true;
  }

  $scope.$watch('green', function (newValue, oldValue) {
    if (! $scope.isValidPercent(newValue)) {
        $scope.green = oldValue;
        return;
    }
    if (parseInt($scope.green) + parseInt($scope.red) === 100) { return; }
    console.log(parseInt($scope.green) + parseInt($scope.red));
    console.log("u-green");
    $scope.red = 100 - $scope.green;
    $scope.updateDataSet();
  });

  $scope.$watch('red', function (newValue, oldValue) {
    if (! $scope.isValidPercent(newValue)) {
        $scope.red = oldValue;
        return;
    }
    if (parseInt($scope.green) + parseInt($scope.red) === 100) { return; }
    console.log(parseInt($scope.green) + parseInt($scope.red));
    console.log("u-red");
    $scope.green = 100 - $scope.red;
    $scope.updateDataSet();
  });

  $scope.updateDataSet = function() {
    console.log("Here");
    $scope.dataSet = [
      { label: 'Green', count: $scope.green }, 
      { label: 'Red', count: $scope.red }
    ];
  }

  $scope.updateDataSet();

}]);
 
app.directive( 'donutChart', [
  function () {
    return {
      restrict: 'E',
      scope: {
        chartdata: '='
      },
      link: function (scope, element) {
        var width = 360;
        var height = 360;
        var radius = Math.min(width, height) / 2;
        var donutWidth = 75;                            
        //var color = d3.scale.category10();
        var color = d3.rgb;

        var svg = d3.select(element[0]).append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr('transform', 'translate(' + (width / 2) + 
            ',' + (height / 2) + ')');

        var arc = d3.svg.arc()
        .innerRadius(radius - donutWidth)             
        .outerRadius(radius);

        var pie = d3.layout.pie()
        .value(function(d) { return d.count; })
        .sort(null);

        var initData = [
            { label: 'Green', count: 50 }, 
            { label: 'Red', count: 50 }
        ];
        var path = svg.selectAll('path')
        .data(pie(initData))
        .enter()
        .append('path')
        .attr('d', arc)
        .attr('fill', function(d, i) { 
            return color(d.data.label);
        })
        .each(function(d) { this._current = d; }); // store the initial angles;

        function arcTween(a) {
          var i = d3.interpolate(this._current, a);
          this._current = i(0);
          return function(t) {
            return arc(i(t));
          };
        }

        scope.render = function(data) {
            console.log("rendering.." + data[0].count + " " + data[1].count);
            svg.selectAll('path')
            .data(pie(data))
            .transition().duration(500)
            .attrTween("d", arcTween);
        }
        
        scope.$watch('chartdata', function(newValue, oldValue) {
          scope.render(newValue);
        }, true);  
    }
    };
  }
]);