let catalogoActual = null;
const LAT_BARRIO = 4.578193;
const LNG_BARRIO = -74.152101;

function enfocarDesdeElemento(elemento) {
    const { lat, lng, nombre, subcategoria, descripcion, ubicacion, fuente, subir } = elemento.dataset;
    const iframe = document.getElementById('iframeGoogleMaps');
    const txt = (ubicacion || '').toLowerCase();
    const sinDireccionExacta = !ubicacion || txt.includes('pendiente') || txt.includes('confirmar') || txt.includes('conexión');

    const consultaMapa = sinDireccionExacta
        ? `${lat},${lng}`
        : encodeURIComponent(`${ubicacion}, Ciudad Bolívar, Bogotá, Colombia`);

    iframe.src = `https://maps.google.com/maps?q=${consultaMapa}&z=17&output=embed`;
    document.getElementById('etiquetaMapaActivo').textContent = nombre;
    document.getElementById('panelCroquisDetalle').innerHTML = `
        <span class="badge bg-dark mb-1">${subcategoria}</span>
        <div class="fw-bold small">${nombre}</div>
        <p class="small mb-1 mt-1">${descripcion}</p>
        <div class="text-muted mb-2" style="font-size: 0.74rem;">
            <strong>Ubicación:</strong> ${ubicacion}<br>
            <strong>Fuente:</strong> ${fuente}
        </div>
        <a href="https://www.google.com/maps/search/?api=1&query=${consultaMapa}" target="_blank" class="btn btn-primary btn-sm w-100">
            Abrir punto en Google Maps ↗
        </a>
    `;

    if (subir === "true") {
        iframe.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

function centrarMapaGeneral() {
    document.getElementById('iframeGoogleMaps').src = `https://maps.google.com/maps?q=${LAT_BARRIO},${LNG_BARRIO}&z=16&output=embed`;
    document.getElementById('etiquetaMapaActivo').textContent = 'Barrio La Coruña';
    document.querySelectorAll('.chip-lugar').forEach(c => c.style.display = 'inline-block');
}

function abrirCatalogo(seccion) {
    const contenedor = document.getElementById('contenedorCatalogo');
    if (catalogoActual === seccion) { cerrarCatalogo(); return; }
    catalogoActual = seccion;

    document.querySelectorAll('.btn-categoria-principal').forEach(b => b.classList.remove('activo'));
    document.getElementById('btn-' + seccion).classList.add('activo');
    document.querySelectorAll('.catalogo-panel').forEach(p => p.style.display = 'none');

    contenedor.style.display = 'block';
    const panelElegido = document.getElementById('catalogo-' + seccion);
    if (panelElegido) {
        panelElegido.style.display = 'block';
        panelElegido.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    const mapaCategorias = {
        recreacion: ['recreacion'],
        comidas: ['gastronomia'],
        turistica: ['referencia', 'historia'],
        orden: ['movilidad', 'seguridad']
    };
    const permitidas = mapaCategorias[seccion] || [];
    document.querySelectorAll('.chip-lugar').forEach(chip => {
        chip.style.display = permitidas.includes(chip.dataset.categoria) ? 'inline-block' : 'none';
    });
}

function cerrarCatalogo() {
    catalogoActual = null;
    document.getElementById('contenedorCatalogo').style.display = 'none';
    document.querySelectorAll('.catalogo-panel').forEach(p => p.style.display = 'none');
    document.querySelectorAll('.btn-categoria-principal').forEach(b => b.classList.remove('activo'));
    centrarMapaGeneral();
}

function filtrarSubComercio(tipo) {
    document.querySelectorAll('.item-comercio').forEach(card => {
        card.style.display = (tipo === 'todos' || card.dataset.subtipo === tipo) ? 'block' : 'none';
    });
}

function buscarEnCatalogo() {
    const texto = document.getElementById('inputBuscador').value.toLowerCase().trim();
    document.querySelectorAll('.chip-lugar').forEach(chip => {
        chip.style.display = (texto === '' || chip.dataset.nombreBusqueda.includes(texto)) ? 'inline-block' : 'none';
    });
    document.querySelectorAll('.item-catalogo').forEach(card => {
        card.style.display = (texto === '' || card.dataset.texto.includes(texto)) ? 'block' : 'none';
    });
}