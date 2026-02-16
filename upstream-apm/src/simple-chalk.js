/**
 * A lightweight, zero-dependency replacement for 'chalk' to improve CLI startup time.
 * Supports basic colors, modifiers, and chaining (e.g., chalk.red.bold).
 *
 * NOTE: This implementation does not support nested styles correctly (resetting inner style
 * resets everything). It is intended for simple top-level logging during startup.
 */

const ANSI_CODES = {
  reset: 0,
  bold: 1,
  dim: 2,
  italic: 3,
  underline: 4,
  inverse: 7,
  hidden: 8,
  strikethrough: 9,
  black: 30,
  red: 31,
  green: 32,
  yellow: 33,
  blue: 34,
  magenta: 35,
  cyan: 36,
  white: 37,
  gray: 90,
  bgBlack: 40,
  bgRed: 41,
  bgGreen: 42,
  bgYellow: 43,
  bgBlue: 44,
  bgMagenta: 45,
  bgCyan: 46,
  bgWhite: 47,
};

const isColorSupported = !process.env.NO_COLOR && (process.stdout.isTTY || process.env.FORCE_COLOR);

function style(codes, text) {
  if (!isColorSupported || codes.length === 0) return text;
  const startCodes = codes.map((c) => `\x1b[${ANSI_CODES[c]}m`).join('');
  return `${startCodes}${text}\x1b[0m`;
}

function createChalk(activeCodes = []) {
  const chalkFn = (...args) => {
    if (args.length === 0) return '';
    return style(activeCodes, args.join(' '));
  };

  Object.keys(ANSI_CODES).forEach((key) => {
    Object.defineProperty(chalkFn, key, {
      get: () => createChalk([...activeCodes, key]),
      enumerable: true,
    });
  });

  return chalkFn;
}

const simpleChalk = createChalk();
export default simpleChalk;
