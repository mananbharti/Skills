// Intentionally faulty offline-sync model. No native app/storage/provider claim.
// The caller's store.read/write contract represents durable local storage;
// this fixture's runner supplies an owned JSON file to observe restart behavior.
export async function flush(store, send) {
  for (const operation of store.read()) {
    store.write(store.read().filter(item => item.id !== operation.id));
    await send({ ...operation, id: operation.id + '-attempt' });
  }
}
