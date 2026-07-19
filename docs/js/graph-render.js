/**
 * Neural Nexus — Knowledge Graph Renderer
 * Interactive visualization of knowledge network with D3.js
 */
(function () {
  'use strict';

  const container = document.getElementById('knowledge-graph');
  
  if (!container) {
    console.error('Knowledge graph container not found!');
    return;
  }

  // Check if D3 is loaded
  if (typeof d3 === 'undefined') {
    console.error('D3.js not loaded!');
    container.innerHTML = '<p style="text-align:center;padding:2rem;color:red;">D3.js not loaded. Check network requests.</p>';
    return;
  }

  // Fetch graph data
  fetch('../graph-data.json')
    .then(r => {
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      return r.json();
    })
    .then(data => {
      render(data);
    })
    .catch(err => {
      console.error('Graph load error:', err);
      container.innerHTML = '<p style="text-align:center;padding:2rem;color:red;">Graph data not found. Run <code>node scripts/build-graph.js</code> first.</p>';
    });

  function render(graph) {
    if (!graph.nodes || !graph.edges) {
      console.error('Invalid graph data structure');
      container.innerHTML = '<p style="text-align:center;padding:2rem;color:red;">Invalid graph data structure</p>';
      return;
    }

    const width = container.clientWidth || 800;
    const height = 600;
    
    // Clear container
    container.innerHTML = '';
    
    // Create SVG
    const svg = d3.select('#knowledge-graph')
      .append('svg')
      .attr('width', width)
      .attr('height', height)
      .attr('viewBox', [0, 0, width, height]);

    // Create main group
    const g = svg.append('g');

    // Add background
    g.append('rect')
      .attr('width', width)
      .attr('height', height)
      .attr('fill', '#f8f9fa');

    // Create color scale for domains
    const color = d3.scaleOrdinal()
      .domain(['concepts', 'entities', 'findings', 'readings', 'ideas', 'comparisons'])
      .range(['#4ecdc4', '#51cf66', '#ffd43b', '#cc5de8', '#ff922b', '#868e96']);

    // Create force simulation
    const simulation = d3.forceSimulation(graph.nodes)
      .force('link', d3.forceLink(graph.edges).id(d => d.id).distance(80))
      .force('charge', d3.forceManyBody().strength(-300))
      .force('center', d3.forceCenter(width / 2, height / 2))
      .force('collision', d3.forceCollide().radius(30));

    // Create links
    const link = g.append('g')
      .selectAll('line')
      .data(graph.edges)
      .join('line')
      .attr('stroke', '#999')
      .attr('stroke-opacity', 0.6)
      .attr('stroke-width', 2);

    // Create nodes
    const node = g.append('g')
      .selectAll('circle')
      .data(graph.nodes)
      .join('circle')
      .attr('r', d => Math.sqrt(d.connections || 1) * 3 + 5)
      .attr('fill', d => color(d.slug.split('/')[0]))
      .attr('stroke', '#fff')
      .attr('stroke-width', 2)
      .call(drag(simulation));

    // Add labels
    const label = g.append('g')
      .selectAll('text')
      .data(graph.nodes)
      .join('text')
      .text(d => d.title)
      .attr('font-size', '12px')
      .attr('dx', 15)
      .attr('dy', 4)
      .attr('fill', '#333');

    // Add click handlers
    node.on('click', (event, d) => {
      const url = d.slug + '.md';
      window.location.href = url;
    });

    // Add hover effects
    node.on('mouseover', function(event, d) {
      d3.select(this)
        .transition()
        .duration(200)
        .attr('r', Math.sqrt(d.connections || 1) * 3 + 8);
      
      // Show tooltip
      const tooltip = d3.select('body')
        .append('div')
        .attr('class', 'tooltip')
        .style('position', 'absolute')
        .style('padding', '8px')
        .style('background', 'rgba(0,0,0,0.8)')
        .style('color', 'white')
        .style('border-radius', '4px')
        .style('font-size', '12px')
        .style('pointer-events', 'none')
        .style('opacity', 0);
      
      tooltip.transition()
        .duration(200)
        .style('opacity', 1);
      
      tooltip.html(`<strong>${d.title}</strong><br/>Connections: ${d.connections || 0}<br/>Click to navigate`)
        .style('left', (event.pageX + 10) + 'px')
        .style('top', (event.pageY - 10) + 'px');
    })
    .on('mouseout', function(event, d) {
      d3.select(this)
        .transition()
        .duration(200)
        .attr('r', Math.sqrt(d.connections || 1) * 3 + 5);
      
      // Remove tooltip
      d3.selectAll('.tooltip').remove();
    });

    // Update positions on tick
    simulation.on('tick', () => {
      link
        .attr('x1', d => d.source.x)
        .attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x)
        .attr('y2', d => d.target.y);
      
      node
        .attr('cx', d => d.x)
        .attr('cy', d => d.y);
      
      label
        .attr('x', d => d.x)
        .attr('y', d => d.y);
    });

    // Add zoom behavior
    const zoom = d3.zoom()
      .scaleExtent([0.1, 4])
      .on('zoom', (event) => {
        g.attr('transform', event.transform);
      });
    
    svg.call(zoom);

    // Add legend
    const legend = g.append('g')
      .attr('transform', `translate(${width - 150}, 20)`);
    
    const legendItems = [
      { domain: 'concepts', color: '#4ecdc4', label: 'Concepts' },
      { domain: 'entities', color: '#51cf66', label: 'Entities' },
      { domain: 'findings', color: '#ffd43b', label: 'Findings' },
      { domain: 'readings', color: '#cc5de8', label: 'Readings' },
      { domain: 'ideas', color: '#ff922b', label: 'Ideas' },
      { domain: 'comparisons', color: '#868e96', label: 'Comparisons' }
    ];
    
    legendItems.forEach((item, i) => {
      legend.append('rect')
        .attr('x', 0)
        .attr('y', i * 20)
        .attr('width', 12)
        .attr('height', 12)
        .attr('fill', item.color);
      
      legend.append('text')
        .attr('x', 18)
        .attr('y', i * 20 + 9)
        .attr('font-size', '12px')
        .attr('fill', '#333')
        .text(item.label);
    });
  }

  // Drag functionality
  function drag(simulation) {
    function dragstarted(event) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      event.subject.fx = event.subject.x;
      event.subject.fy = event.subject.y;
    }
    
    function dragged(event) {
      event.subject.fx = event.x;
      event.subject.fy = event.y;
    }
    
    function dragended(event) {
      if (!event.active) simulation.alphaTarget(0);
      event.subject.fx = null;
      event.subject.fy = null;
    }
    
    return d3.drag()
      .on('start', dragstarted)
      .on('drag', dragged)
      .on('end', dragended);
  }
})();