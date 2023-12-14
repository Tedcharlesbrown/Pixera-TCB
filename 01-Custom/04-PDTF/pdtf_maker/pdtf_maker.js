class ParameterFields {
    constructor(parentElement) {
        this.name = document.createElement("input");
        this.name.type = "text";
        this.name.classList.add("parameter-name");
        this.name.placeholder = "Parameter Name";
        this.min = document.createElement("input");
        this.min.type = "number";
        this.min.classList.add("parameter-min");
        this.min.placeholder = "Min Value";
        this.max = document.createElement("input");
        this.max.type = "number";
        this.max.classList.add("parameter-max");
        this.max.placeholder = "Max Value";
        this.default = document.createElement("input");
        this.default.type = "number";
        this.default.classList.add("parameter-default");
        this.default.placeholder = "Default Value";
        parentElement.appendChild(this.name);
        parentElement.appendChild(this.min);
        parentElement.appendChild(this.max);
        parentElement.appendChild(this.default);
    }
}

class DeleteButton {
    constructor(parentElement) {
        this.button = document.createElement("button");
        this.button.textContent = "X";
        this.button.classList.add("delete-button");
        this.button.onclick = () => parentElement.remove();
        return this.button;
    }
}

class MoveUpButton {
    constructor(elementToMove) {
        this.button = document.createElement("button");
        this.button.textContent = "↑";
        this.button.classList.add("move-up-button");
        this.button.onclick = () => moveElementUp(elementToMove);
        return this.button;
    }
}

class MoveDownButton {
    constructor(elementToMove) {
        this.button = document.createElement("button");
        this.button.textContent = "↓";
        this.button.classList.add("move-down-button");
        this.button.onclick = () => moveElementDown(elementToMove);
        return this.button;
    }
}

let pdtfData = { nodes: [] };

function addParam() {
    const pdtfBuilder = document.getElementById("pdtfBuilder");
    const paramDiv = document.createElement("div");
    paramDiv.classList.add("parameter");
    const paramFields = new ParameterFields(paramDiv);

    // Add control buttons
    const deleteButton = new DeleteButton(paramDiv);
    paramDiv.insertBefore(deleteButton, paramDiv.firstChild);
    const moveUpButton = new MoveUpButton(paramDiv);
    const moveDownButton = new MoveDownButton(paramDiv);
    paramDiv.appendChild(moveUpButton);
    paramDiv.appendChild(moveDownButton);

    pdtfBuilder.appendChild(paramDiv);
}

function addFolder() {
    const pdtfBuilder = document.getElementById("pdtfBuilder");
    const folderDiv = document.createElement("div");
    folderDiv.classList.add("folder");

    // Create a header for the folder to contain the folder name and add button
    const folderHeader = document.createElement("div");
    folderHeader.innerHTML = `
          <input type="text" class="folder-name" placeholder="Folder Name">
          <button type="button" class="control-button" onclick="addParamToFolder(this.parentNode)">Add Parameter</button>
      `;

    folderDiv.appendChild(folderHeader);

    const deleteButton = new DeleteButton(folderDiv);
    folderHeader.insertBefore(deleteButton, folderHeader.firstChild);

    const moveUpButton = new MoveUpButton(folderDiv);
    const moveDownButton = new MoveDownButton(folderDiv);
    folderHeader.appendChild(moveUpButton);
    folderHeader.appendChild(moveDownButton);

    pdtfBuilder.appendChild(folderDiv);
}

function moveElementUp(element) {
    const previousElement = element.previousElementSibling;

    // Check if the element is a child parameter
    if (element.classList.contains('child-parameter')) {
        // Prevent moving above the parent folder's header
        if (!previousElement || previousElement.tagName === 'DIV') {
            return;
        }
    } else {
        // Check for top-level parameters
        // Prevent moving above the control buttons
        if (!previousElement || previousElement.classList.contains('control-button')) {
            return;
        }
    }

    element.parentNode.insertBefore(element, previousElement);
}



function moveElementDown(element) {
    const nextElement = element.nextElementSibling;
    if (nextElement) {
        element.parentNode.insertBefore(nextElement, element);
    }
}

function addParamToFolder(button) {
    const folderDiv = button.parentNode;
    const paramDiv = document.createElement("div");
    paramDiv.classList.add("child-parameter");
    const paramFields = new ParameterFields(paramDiv);

    // Add control buttons to the parameter
    const deleteButton = new DeleteButton(paramDiv);
    paramDiv.insertBefore(deleteButton, paramDiv.firstChild);
    const moveUpButton = new MoveUpButton(paramDiv);
    const moveDownButton = new MoveDownButton(paramDiv);
    paramDiv.appendChild(moveUpButton);
    paramDiv.appendChild(moveDownButton);

    // Insert the parameter div inside the folder
    folderDiv.appendChild(paramDiv);
}

function downloadPDTF() {
    generatePDTF();

    const output = document.getElementById("output").value;
    const blob = new Blob([output], { type: "text/xml;charset=utf-8" });
    
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "pdtf.xml";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

function generatePDTF() {
    pdtfData.nodes = []; // Reset the data structure
    const pdtfBuilder = document.getElementById("pdtfBuilder");

    Array.from(pdtfBuilder.children).forEach((child) => {
        if (child.classList.contains("folder")) {
            // Process folder
            const folder = {
                name: child.querySelector("input[type='text']").value,
                params: []
            };

            child.querySelectorAll(".parameter").forEach((paramDiv) => {
                const inputs = paramDiv.querySelectorAll("input");
                folder.params.push({
                    name: inputs[0].value,
                    min: inputs[1].value,
                    max: inputs[2].value,
                    default: inputs[3].value
                });
            });

            pdtfData.nodes.push(folder);
        } else if (child.classList.contains("parameter")) {
            // Process top-level parameter
            const inputs = child.querySelectorAll("input");
            pdtfData.nodes.push({
                name: inputs[0].value,
                min: inputs[1].value,
                max: inputs[2].value,
                default: inputs[3].value
            });
        }
    });

    const output = document.getElementById("output");
    output.value = generatePDTFXML(pdtfData);
}

function generatePDTFXML(data) {
    let xml = '<?xml version="1.0" encoding="utf-8"?>\n<nodes>\n';
    data.nodes.forEach((node) => {
        if (node.params) {
            xml += `  <folder name="${node.name}">\n`;
            node.params.forEach((param) => {
                xml += `    <param name="${param.name}" min="${param.min}" max="${param.max}" default="${param.default}"/>\n`;
            });
            xml += "  </folder>\n";
        } else {
            xml += `  <param name="${node.name}" min="${node.min}" max="${node.max}" default="${node.default}"/>\n`;
        }
    });
    xml += "</nodes>";
    return xml;
}
