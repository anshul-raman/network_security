const atbashKey = {};
const charCode_a = "a".charCodeAt(0);
const charCode_z = "z".charCodeAt(0);
const charCode_A = "A".charCodeAt(0);
const charCode_Z = "Z".charCodeAt(0);

for (let i = charCode_A, j = 0; i <= charCode_Z; i++, j++) {
  atbashKey[String.fromCharCode(i)] = String.fromCharCode(charCode_Z - j);
}

for (let i = charCode_a, j = 0; i <= charCode_z; i++, j++) {
  atbashKey[String.fromCharCode(i)] = String.fromCharCode(charCode_z - j);
}

const atBash = (text) => {
  // console.log("calling atbash function");
  if (typeof text != "string") return "";

  let res = "";

  for (let i = 0; i < text.length; i++) {
    if (text[i] in atbashKey) {
      res += atbashKey[text[i]];
    } else {
      res += text[i];
    }
  }

  return res;
};

export default atBash;
