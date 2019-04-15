function descriptionOnChange() {
    var description = Xrm.Page.getAttribute('description').getValue();
    var iFrame = Xrm.Page.ui.controls.get('WebResource_opptyhtml').getObject();
    var element = iFrame.contentWindow.document.getElementById('description');
    element.value = description;
}



const values = {
    opptyname: "Pero",
    descript: "opiscina"
}
const keys = Object.keys(values)
const length = keys.length

for(let i = 0; i < length; i++){
    const key = keys[i]
    document.getElementsByName(key)[0].value = values[key]
    }