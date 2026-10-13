// Corrected deterministic server-state model; authenticated principal is a precondition.
export function apply(state, principal, message) {
  const player = state.players[principal];
  if (!player || !message || message.player !== principal || message.epoch !== player.epoch)
    throw new Error('invalid player/session');
  if (!Number.isSafeInteger(message.sequence) || message.sequence < 1 ||
      !Number.isInteger(message.dx) || Math.abs(message.dx) > 1)
    throw new Error('invalid input');
  if (message.sequence <= player.last) return 'duplicate';
  if (message.sequence !== player.last + 1) throw new Error('sequence gap; resync required');
  player.x += message.dx;
  player.last = message.sequence;
  return 'applied';
}
