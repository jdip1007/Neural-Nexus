/**
 * Neural Nexus — Knowledge Graph Renderer
 * Loads graph-data.json and renders a D3.js force-directed graph.
 * Activates only on the graph page (checks for #knowledge-graph container).
 */
(function () {
  'use strict';

  const container = document.getElementById('knowledge-graph');
  if (!container) return;

  const DOMAIN_COLORS = {
    ai: '#4ecdc4', ml: '#4ecdc4', llm: '#4ecdc4', 'deep-learning': '#4ecdc4', nlp: '#4ecdc4',
    biotech: '#51cf66', genomics: '#51cf66',
    finance: '#ffd43b', trading: '#ffd43b', economics: '#ffd43b',
    psychology: '#cc5de8', neuroscience: '#cc5de8',
    devops: '#ff922b', infrastructure: '#ff922b',
    hermes: '#ff6b6b', automation: '#ff6b6b',
    general: '#868e96'
  };

  function getColor(node) {
    return DOMAIN_COLORS[node.domain] || DOMAIN_COLORS['general'];
  }

  function getRadius(node) {
    return 6 + Math.sqrt(node.inboundLinks + node.outboundLinks) * 3;
  }

  function render(graph) {
    const width = container.clientWidth || 800;
    const height = 600;

    // Update stats table
    const cells = document.querySelectorAll('table td');
    if (cells[0]) cells[0].textContent = graph.metadata.totalNodes;
    if (cells[1]) cells[1].textContent = graph.metadata.totalEdges;
    if (cells[2]) {
      const orphans = graph.nodes.filter(n => n.inboundLinks === 0 && n.outboundLinks === 0);
      cells[2].textContent = orphans.length;
    }

    const svg = d3.select('#knowledge-graph')
      .append('svg')
      .attr('width', width)
      .attr('height', height)
      .attr('viewBox', [0, 0, width, height]);

    const g = svg.append('g');
    svg.call(d3.zoom().scaleExtent([0.1, 4]).on('zoom', (e) => {
      g.attr('transform', e.transform);
    }));

    const simulation = d3.forceSimulation(graph.nodes)
      .force('link', d3.forceLink(graph.edges).id(d => d.id).distance(80))
      .force('charge', d3.forceManyBody().strength(-200))
      .force('center', d3.forceCenter(width / 2, height / 2))
      .force('collide', d3.forceCollide().radius(d => getRadius(d) + 5));

    const link = g.append('g')
      .selectAll('line')
      .data(graph.edges)
      .join('line')
      .attr('stroke', '#999')
      .attr('stroke-opacity', 0.4)
      .attr('stroke-width', 1);

    const node = g.append('g')
      .selectAll('circle')
      .data(graph.nodes)
      .join('circle')
      .attr('r', d => getRadius(d))
      .attr('fill', d => getColor(d))
      .attr('stroke', '#fff')
      .attr('stroke-width', 1.5)
      .style('cursor', 'pointer')
      .on('click', (event, d) => { window.location.href = d.url; })
      .on('mouseover', function (event, d) {
        d3.select(this).attr('stroke-width', 3);
        showTooltip(event, d);
      })
      .on('mouseout', function () {
        d3.select(this).attr('stroke-width', 1.5);
        hideTooltip();
      });

    node.append('title').text(d => d.title);

    node.call(d3.drag()
      .on('start', (event, d) => {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x; d.fy = d.y;
      })
      .on('drag', (event, d) => { d.fx = event.x; d.fy = event.y; })
      .on('end', (event, d) => {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null; d.fy = null;
      }));

    let tooltip = d3.select('#graph-tooltip');
    if (tooltip.empty()) {
      tooltip = d3.select('body').append('div')
        .attr('id', 'graph-tooltip')
        .style('position', 'absolute')
        .style('background', 'rgba(0,0,0,0.8)')
        .style('color', '#fff')
        .style('padding', '6px 10px')
        .style('border-radius', '4px')
        .style('font-size', '12px')
        .style('pointer-events', 'none')
        .style('opacity', 0);
    }

    function showTooltip(event, d) {
      tooltip
        .style('opacity', 1)
        .html(`<strong>${d.title}</strong><br>${d.type} · ${d.domain}<br>${d.inboundLinks + d.outboundLinks} connections`)
        .style('left', (event.pageX + 10) + 'px')
        .style('top', (event.pageY - 10) + 'px');
    }

    function hideTooltip() { tooltip.style('opacity', 0); }

    simulation.on('tick', () => {
      link
        .attr('x1', d => d.source.x).attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
      node
        .attr('cx', d => d.x).attr('cy', d => d.y);
    });
  }

  const init = () => {
    // Use relative path — works on both local serve and GitHub Pages
    fetch('graph-data.json')
      .then(r => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then(data => render(data))
      .catch(err => {
        container.innerHTML = '<p style="text-align:center;padding:2rem;color:#888;">Graph data not found. Run <code>node scripts/build-graph.js</code> first.</p>';
        console.error('Graph load error:', err);
      });
  };

  if (typeof document$ !== 'undefined') {
    document$.subscribe(init);
  } else {
    document.addEventListener('DOMContentLoaded', init);
  }
})();
