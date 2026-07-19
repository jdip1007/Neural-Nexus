// Graph visualization using D3.js
document.addEventListener('DOMContentLoaded', function() {
  const container = d3.select('#knowledge-graph');
  const width = container.node().getBoundingClientRect().width;
  const height = 600;

  // Clear previous content
  container.selectAll('*').remove();

  const svg = container.append('svg')
    .attr('width', width)
    .attr('height', height);

  // Load graph data
  fetch('/graph-data.json')
    .then(response => response.json())
    .then(data => {
      // Create color scale
      const colorScale = d3.scaleOrdinal()
        .domain(['ai', 'biotech', 'finance', 'devops', 'psychology', 'general'])
        .range(['#4ecdc4', '#51cf66', '#ff6b6b', '#4dabf7', '#f06595', '#868e96']);

      // Create force simulation
      const simulation = d3.forceSimulation(data.nodes)
        .force('link', d3.forceLink(data.edges).id(d => d.id).distance(100))
        .force('charge', d3.forceManyBody().strength(-300))
        .force('center', d3.forceCenter(width / 2, height / 2))
        .force('collision', d3.forceCollide().radius(30));

      // Create links
      const link = svg.append('g')
        .attr('class', 'links')
        .selectAll('line')
        .data(data.edges)
        .enter().append('line')
        .attr('stroke', '#999')
        .attr('stroke-opacity', 0.6)
        .attr('stroke-width', 2);

      // Create nodes
      const node = svg.append('g')
        .attr('class', 'nodes')
        .selectAll('circle')
        .data(data.nodes)
        .enter().append('circle')
        .attr('r', d => Math.max(8, Math.min(20, 5 + d.inboundLinks)))
        .attr('fill', d => colorScale(d.domain))
        .attr('stroke', '#fff')
        .attr('stroke-width', 2)
        .call(d3.drag()
          .on('start', dragstarted)
          .on('drag', dragged)
          .on('end', dragended));

      // Add labels
      const label = svg.append('g')
        .attr('class', 'labels')
        .selectAll('text')
        .data(data.nodes)
        .enter().append('text')
        .text(d => d.title)
        .attr('font-size', '12px')
        .attr('dx', 15)
        .attr('dy', 4)
        .attr('fill', '#333');

      // Add click behavior
      node.on('click', function(event, d) {
        window.location.href = d.url;
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

      // Drag functions
      function dragstarted(event, d) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
      }

      function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
      }

      function dragended(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
      }

      // Add zoom behavior
      const zoom = d3.zoom()
        .scaleExtent([0.1, 4])
        .on('zoom', function(event) {
          svg.attr('transform', event.transform);
        });

      svg.call(zoom);
    })
    .catch(error => {
      console.error('Error loading graph data:', error);
      container.append('text')
        .attr('x', width / 2)
        .attr('y', height / 2)
        .attr('text-anchor', 'middle')
        .attr('fill', '#666')
        .text('Graph data not available. Run build script first.');
    });
});