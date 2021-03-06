d3.custom = {}

d3.custom.donutChart = function module() {
    var width = 360;
    var height = 360;
    var radius = Math.min(width, height) / 2;
    var donutWidth = 75;                            
    //var color = d3.scale.category10();
    var color = d3.rgb;

    var svg = d3.select(this)
    .append('svg')
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

    var path = svg.selectAll('path')
    .data(pie(dataset))
    .enter()
    .append('path')
    .attr('d', arc)
    .attr('fill', function(d, i) { 
        return color(d.data.label);
    });
}