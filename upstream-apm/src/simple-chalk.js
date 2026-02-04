// A lightweight replacement for chalk to improve startup time
// Supports only the subset of colors/styles used in this project

const codes = {
  reset: [0, 0],
  bold: [1, 22],
  underline: [4, 24],
  red: [31, 39],
  green: [32, 39],
  yellow: [33, 39],
  blue: [34, 39],
  cyan: [36, 39],
  white: [37, 39],
  gray: [90, 39],
};

// Check if we should support color
// We rely on standard env vars and TTY status
const supportsColor =
  (process.stdout && process.stdout.isTTY) &&
  !process.env.NO_COLOR;

function createChalk(activeKeys = []) {
  const builder = (...inputs) => {
    // Handle multiple arguments, join with space (mimic console.log/chalk)
    const str = inputs.map(input => String(input)).join(' ');

    // If color is not supported, return plain text
    if (!supportsColor) {
      return str;
    }

    let opens = '';
    let closes = '';

    for (const key of activeKeys) {
      const [o, c] = codes[key];
      opens += `\x1b[${o}m`;
      closes = `\x1b[${c}m` + closes;
    }

    return opens + str + closes;
  };

  for (const key of Object.keys(codes)) {
    if (key === 'reset') continue;
    Object.defineProperty(builder, key, {
      get() {
        return createChalk([...activeKeys, key]);
      }
    });
  }

  return builder;
}

export default createChalk();
