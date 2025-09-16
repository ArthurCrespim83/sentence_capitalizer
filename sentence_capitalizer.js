function capitalize(paragraph) {
  let result = "";
  let capitalizeNext = true;

  for (let i = 0; i < paragraph.length; i++) {
    const char = paragraph[i];
    
    // Check if the current character is a letter
    const isLetter = (char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z');
    
    if (capitalizeNext && isLetter) {
      result += char.toUpperCase();
      capitalizeNext = false;
    } else {
      result += char;
    }

    // Check if the current character ends a sentence
    if (char === '.' || char === '?' || char === '!') {
      capitalizeNext = true;
    }
  }

  return result;
}

const myParagraph = "hello world. this is an example? and here's another one!";
const correctedParagraph = capitalize(myParagraph);
console.log(correctedParagraph); // Saída esperada: "Hello world. This is an example? And here's another one!"



