d3.csv("dataCSV.csv", function (data) { 

    var height = 400;
    var width = 800;
    counter = 0;

    data.forEach(function(d) {
       d.tsStamp = +d.tsStamp;
       d.respiration_belt = +d.respiration_belt;
       d.blood_pressure = +d.blood_pressure;
       counter = counter + 1;
    });
   
    var maxTime = d3.max(data, function(d) { return d.tsStamp; });
    var minTime = d3.min(data, function(d) { return d.tsStamp; });
    var maxResp = d3.max(data, function(d) { return d.respiration_belt; });
    var minResp = d3.min(data, function(d) { return d.respiration_belt; });
    var maxBP = d3.max(data, function(d) { return d.blood_pressure; });
    var minBP = d3.min(data, function(d) { return d.blood_pressure; });

    // console.log(maxTime);
    // console.log(minTime);
    // console.log(maxResp);
    // console.log(minResp);
    // console.log(minBP);
    // console.log(maxBP);

    // console.log(counter);
    
    var y = d3.scaleLinear()
        .domain([minResp, maxResp])
        .range([height, 0]);
    
    var y1 = d3.scaleLinear()
        .domain([minBP, maxBP])
        .range([height, 0])

    var x = d3.scaleLinear()
        .domain([minTime, maxTime])
        .range([0, width]);

    var yAxis = d3.axisLeft(y);
    var xAxis = d3.axisBottom(x);

    var svg = d3.select('body').append('svg')
        .attr('height', '55%')
        .attr('width', '100%')

    // var svg1 = d3.select('body').append('svg')
    //     .attr('height', '100%')
    //     .attr('width', '100%')

    var chartGroup = svg.append('g')
        .attr('transform', 'translate(500, 50)');
    // var chartGroup1 = svg1.append('g')
    //     .attr('transform', 'translate(100, 50)');

    var line = d3.line()
        .x(function(d) { return x(d.tsStamp);})
        .y(function(d) { return y(d.respiration_belt);});
    
    var line2 = d3.line()
        .x(function(d) { return x(d.tsStamp);})
        .y(function(d) { return y(d.blood_pressure);});

    chartGroup.append('path').attr('d', line(data));
    //chartGroup.append('path').attr('d', line2(data));
    chartGroup.append('g').attr('class', 'x axis').attr('transform', 'translate(0, '+height+')').call(xAxis);
    chartGroup.append('g').attr('class', 'y axis').call(yAxis);
    chartGroup.append("text")      // text label for the x axis
        .attr("x", 400)
        .attr("y", 440)
        .style("text-anchor", "middle")
        .text("Time (Seconds)");
    svg.append("text")      // text label for the x axis
        .attr("x", 300)
        .attr("y", 250)
        .style("text-anchor", "left")
        .text("Respiration");

    // chartGroup1.append('path').attr('d', line(data));
    // chartGroup1.append('path').attr('d', line2(data));
    // chartGroup1.append('g').attr('class', 'x axis').attr('transform', 'translate(0, '+height+')').call(xAxis);
    // chartGroup1.append('g').attr('class', 'y axis').call(yAxis);
    // chartGroup1.append("text")      // text label for the x axis
    //     .attr("x", 400)
    //     .attr("y", 500)
    //     .style("text-anchor", "middle")
    //     .text("Date");
    // svg.append("text")      // text label for the x axis
    //     .attr("x", 40)
    //     .attr("y", 250)
    //     .style("text-anchor", "left")
    //     .text("Date");
});

d3.csv("dataCSV.csv", function (data) { 

    var height = 400;
    var width = 800;

    data.forEach(function(d) {
       d.tsStamp = +d.tsStamp;
       d.blood_pressure = +d.blood_pressure;
    });
   
    var maxTime = d3.max(data, function(d) { return d.tsStamp; });
    var minTime = d3.min(data, function(d) { return d.tsStamp; });
    var maxBP = d3.max(data, function(d) { return d.blood_pressure; });
    var minBP = d3.min(data, function(d) { return d.blood_pressure; });
    
    var y = d3.scaleLinear()
        .domain([minBP, maxBP])
        .range([height, 0]);

    var x = d3.scaleLinear()
        .domain([minTime, maxTime])
        .range([0, width]);

    var yAxis = d3.axisLeft(y);
    var xAxis = d3.axisBottom(x);

    var svg = d3.select('body').append('svg')
        .attr('height', '55%')
        .attr('width', '100%')

    var chartGroup = svg.append('g')
        .attr('transform', 'translate(500, 50)');

    var line = d3.line()
        .x(function(d) { return x(d.tsStamp);})
        .y(function(d) { return y(d.blood_pressure);});

    chartGroup.append('path').attr('d', line(data));
    chartGroup.append('g').attr('class', 'x axis').attr('transform', 'translate(0, '+height+')').call(xAxis);
    chartGroup.append('g').attr('class', 'y axis').call(yAxis);
    chartGroup.append("text")      // text label for the x axis
        .attr("x", 400)
        .attr("y", 440)
        .style("text-anchor", "middle")
        .text("Time (Seconds)");
    svg.append("text")      // text label for the x axis
        .attr("x", 300)
        .attr("y", 250)
        .style("text-anchor", "left")
        .text("Blood Pressure");
});

d3.csv("dataCSV.csv", function (data) { 

    var height = 400;
    var width = 800;

    data.forEach(function(d) {
       d.tsStamp = +d.tsStamp;
       d.skin_conductivity = +d.skin_conductivity;
    });
   
    var maxTime = d3.max(data, function(d) { return d.tsStamp; });
    var minTime = d3.min(data, function(d) { return d.tsStamp; });
    var maxGSR = d3.max(data, function(d) { return d.skin_conductivity; });
    var minGSR = d3.min(data, function(d) { return d.skin_conductivity; });
    
    var y = d3.scaleLinear()
        .domain([minGSR, maxGSR])
        .range([height, 0]);

    var x = d3.scaleLinear()
        .domain([minTime, maxTime])
        .range([0, width]);

    var yAxis = d3.axisLeft(y);
    var xAxis = d3.axisBottom(x);

    var svg = d3.select('body').append('svg')
        .attr('height', '55%')
        .attr('width', '100%')

    var chartGroup = svg.append('g')
        .attr('transform', 'translate(500, 50)');

    var line = d3.line()
        .x(function(d) { return x(d.tsStamp);})
        .y(function(d) { return y(d.skin_conductivity);});

    chartGroup.append('path').attr('d', line(data));
    chartGroup.append('g').attr('class', 'x axis').attr('transform', 'translate(0, '+height+')').call(xAxis);
    chartGroup.append('g').attr('class', 'y axis').call(yAxis);
    chartGroup.append("text")      // text label for the x axis
        .attr("x", 400)
        .attr("y", 440)
        .style("text-anchor", "middle")
        .text("Time (Seconds)");
    svg.append("text")      // text label for the x axis
        .attr("x", 250)
        .attr("y", 250)
        .style("text-anchor", "left")
        .text("Skin Conductivity (Siemens)");
});

d3.csv("dataCSV.csv", function (data) { 

    var height = 400;
    var width = 800;

    data.forEach(function(d) {
       d.tsStamp = +d.tsStamp;
       d.pulse = +d.pulse;
    });
   
    var maxTime = d3.max(data, function(d) { return d.tsStamp; });
    var minTime = d3.min(data, function(d) { return d.tsStamp; });
    var maxPulse = d3.max(data, function(d) { return d.pulse; });
    var minPulse = d3.min(data, function(d) { return d.pulse; });
    
    var y = d3.scaleLinear()
        .domain([minPulse, maxPulse])
        .range([height, 0]);

    var x = d3.scaleLinear()
        .domain([minTime, maxTime])
        .range([0, width]);

    var yAxis = d3.axisLeft(y);
    var xAxis = d3.axisBottom(x);

    var svg = d3.select('body').append('svg')
        .attr('height', '55%')
        .attr('width', '100%')

    var chartGroup = svg.append('g')
        .attr('transform', 'translate(500, 50)');

    var line = d3.line()
        .x(function(d) { return x(d.tsStamp);})
        .y(function(d) { return y(d.pulse);});

    chartGroup.append('path').attr('d', line(data));
    chartGroup.append('g').attr('class', 'x axis').attr('transform', 'translate(0, '+height+')').call(xAxis);
    chartGroup.append('g').attr('class', 'y axis').call(yAxis);
    chartGroup.append("text")      // text label for the x axis
        .attr("x", 400)
        .attr("y", 440)
        .style("text-anchor", "middle")
        .text("Time (Seconds)");
    svg.append("text")      // text label for the x axis
        .attr("x", 300)
        .attr("y", 250)
        .style("text-anchor", "left")
        .text("Pulse Rate");
});