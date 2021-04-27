import { TennisGame } from '../src';
import { checkAllScores } from './utils';

describe('TennisGame', function () {
  it('should correctly check all the scores for game', function () {
    checkAllScores(() => new TennisGame('player1', 'player2'));
  });
});
