// Corrected local model; durable storage and authenticated/idempotent server are preconditions.
export async function flush(store, send) {
  for (const operation of store.read()) {
    await send(operation); // Stable operation identity across retries; remove only after ack.
    store.write(store.read().filter(item => item.id !== operation.id));
  }
}
