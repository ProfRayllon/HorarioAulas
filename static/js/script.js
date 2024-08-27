async function carregarHorarios() {
    const response = await fetch('/horarios_do_dia');
    const horarios = await response.json();
    
    const listaHorarios = document.getElementById('lista-horarios');
    listaHorarios.innerHTML = "";  // Limpa a lista antes de adicionar novos itens
    
    if (horarios.length === 0) {
        const listItem = document.createElement('li');
        listItem.textContent = "Sem aulas no momento";
        listaHorarios.appendChild(listItem);
    } else {
        horarios.forEach(horario => {
            const listItem = document.createElement('li');
            listItem.textContent = `${horario[2]} (Sala: ${horario[3]}) - ${horario[0]} às ${horario[1]}`;
            listaHorarios.appendChild(listItem);
        });
    }
}

carregarHorarios();  // Carrega os horários quando a página é carregada
