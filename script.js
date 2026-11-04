const prompt = "hola qué es la ia"
const res = await fetch("http://localhost:8000/chat/"+prompt)
console.log(prompt)
const datos = await res.json()

console.log(datos)