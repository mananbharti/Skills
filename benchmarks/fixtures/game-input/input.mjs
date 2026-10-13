// Intentionally faulty server-state model, not a socket/game-engine adapter.
// principal is authenticated upstream; message content is untrusted.
export function apply(state, principal, message) {
  const player = state.players[message.player];
  player.x += message.dx;
  player.last = message.sequence;
  return 'applied';
}
