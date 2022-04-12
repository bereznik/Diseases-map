var map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    view: new ol.View({
      center: ol.proj.fromLonLat([-43.1729, -22.9068]),
      zoom: 4
    })
  });


  myStyle = new ol.style.Style({
    image: new ol.style.Circle({
        radius: 12,
        fill: new ol.style.Fill({color: 'orange'}),
        stroke: new ol.style.Stroke({
            color: [255,255,255], width: 1
        })
    })
})

  var layer = new ol.layer.Vector({
    source: new ol.source.Vector({
        features: [
            new ol.Feature({
                geometry: new ol.geom.Point(ol.proj.fromLonLat([-43.1729, -22.9068]))
            }),
            new ol.Feature({
                geometry: new ol.geom.Point(ol.proj.fromLonLat([-65.8561,-3.4168]))
            })
        ]
    }),
        style: myStyle
  });
  map.addLayer(layer);


  var container = document.getElementById('popup');
  var content = document.getElementById('popup-content');
  var closer = document.getElementById('popup-closer');

  var overlay = new ol.Overlay({
      element: container,
      autoPan: true,
      autoPanAnimation: {
          duration: 250
      }
  });
  map.addOverlay(overlay);

  closer.onclick = function() {
      overlay.setPosition(undefined);
      closer.blur();
      return false;
  };

  map.on('singleclick', function (event) {
  if (map.hasFeatureAtPixel(event.pixel) === true) {
      var coordinate = event.coordinate;

      content.innerHTML = `<table class="table table-dark">
      <thead>
        <tr>
          <th scope="col">Doença</th>
          <th scope="col">Gravidade</th>
          <th scope="col">Municipio</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">Dengue</th>
          <td>Média</td>
          <td>RJ</td>
        </tr>
      </tbody>
    </table>`;

      overlay.setPosition(coordinate);
  } else {
      overlay.setPosition(undefined);
      closer.blur();
  }
});