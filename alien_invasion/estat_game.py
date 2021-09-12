class GameStats():
    """Armazena dados estatísticos da Invasão Alienígena"""

    def __init__(self, ai_configuracoes):
        """Inicializa os dados estatísticos"""
        self.ai_configuracoes = ai_configuracoes
        self.reset_stats()
        self.game_active = False
        self.pontuacao_maxima = 0

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo"""
        self.naves_abatidas = self.ai_configuracoes.nave_limit
        # Para reiniciar a pontuação sempre que um novo jogo começar
        self.pontos = 0
        self.nivel = 1


