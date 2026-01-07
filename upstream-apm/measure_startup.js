const start = process.hrtime.bigint();
import('./src/index.js').then(() => {
  const end = process.hrtime.bigint();
  console.log('Startup time (ns):', end - start);
  process.exit(0);
});
