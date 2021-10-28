# Racismômetro (data) - Portuguese version

[![CICD](https://github.com/Racisometro/data/actions/workflows/main.yml/badge.svg)](https://github.com/Racisometro/data/actions/workflows/main.yml)

## Set-up

1. Faça o clone do projeto para sua máquina local `git clone`
2. Faça o download do python 3 através do site ou com o homebrew
3. Abra o terminal (bash/zsh) na pasta do projeto
4. Execute os comandos:
    `python3 -m venv ./venv`
    `source venv/bin/activate`
    `pip install -r requirements.txt`
5. Se está usando o VS Code, instale a extensão do Python. Após a instalação, use `cmd + shift + P` e selecione a opção **Python: select interpreter** para escolher a venv desejada.
6. Peça a um membro do projeto as variáveis de ambiente.

## Um pouco do nosso processo de CI/CD

Existem duas branches principais no repositório (`develop`, `main`). Isso foi necessário para continuar com a versão free do Heroku, que nos permite ter apenas 5 apps na conta (sem info de pagamento), e também tem apenas 3 etapas de deploy em sua versão free (`develop`, `staging`, `production`).

O push está liberado para a branch develop, que tem um pipeline de CD no Heroku, onde faz o deploy automático para a etapa `develop` do Heroku.

O pipeline do Heroku tem 3 etapas, e é usado como nossos quality gates. O primeiro é `develop`, onde estão todas as features não testadas. Após o deskcheck, o app é promovido para `staging`, onde são realizados os testes, e após isso, o app é promovido para `production`, onde o app é apresentado para os stakeholders.

Quando é realizado um merge (através de pull request) para a `main`, o Heroku atualiza automaticamente outro pipeline, que faz o deploy para a etapa de `production` do Heroku. Este outro pipeline do Heroku é o responsável pela aplicação final.

### Commits

Os commits na branch de develop devem ser realizados seguindo o padrão semantic-release, onde usamos:

`git commit -m 'fix: CARD - descrição da correção'`
`git commit -m 'feat: CARD - descrição da feature'`

**OBS**: Para outros comandos, verifique a [documentação](https://github.com/semantic-release/semantic-release).

### Check-in dance

Para realizar check-in/commit, toda pessoa desenvolvedora deve seguir os seguintes passos:

Dicionário:
TIPO: Tipo do commit, veja a seção Commits.
CARD: Número/Descrição do card no Trello.

1. Rode os testes `pytest`
1. Faça o commit local
    1. Adicione os arquivos em staging `git add <nomeDoArquivo> -A` or `git add -p`
    1. Comite os arquivos `git commit -m "TIPO: CARD - sua mensagem de commit"`
1. Verifique se o workflow no GitHub está verde
1. Atualize o código `git pull --rebase`
    1. Corrija os arquivos que tiverem conflitos
	    1. `git add <arquivos corrigidos>`
	    1. `git rebase --continue`
    1. Rode todos os testes novamente `pytest`
1. Envie seu código `git push`
1. Verifique se o workflow no GitHub permanece verde
    1. Vermelho? Conserte imediatamente ou desfaça as alterações `git revert`

### Como contribuir?

Para contribuir com o projeto, uma pessoa desenvolvedora pode:

* Se identificar erros/melhorias na codificação, abrir uma issue no GitHub
* Abrir pull requests para a branch `develop`

# Racismômetro (data) - English version

[![CICD](https://github.com/Racisometro/frontend/actions/workflows/main.yml/badge.svg)](https://github.com/Racisometro/frontend/actions/workflows/main.yml)

## Set-up


2. Install dependencies `npm install`
3. Ask a contributor for the environment variables

1. Clone the project to your local machine `git clone`
2. Download python3 from Python website or install with homebrew
3. Open your terminal (bash/zsh) and navigate to the project folder
4. Run the commands:
    `python3 -m venv ./venv`
    `source venv/bin/activate`
    `pip install -r requirements.txt`
5. If you're using VS Code, install Python extension on it. Then, press `cmd + shift + P` and select option **Python: select interpreter** and choose your virtualenv that was created with pipenv
6. Ask a project member for the environment variables.

## About our CI/CD process

There is two main branches in the repo (`develop`, `main`). That was necessary to use the free Heroku licence, that allows only five apps on the account (without billing info), and also has only three stages of deploy (`develop`, `staging`, `production`).

For members, the push can be done in the `develop` branch, that has a pipeline in Heroku, which does the automatic deploy.

Heroku pipeline has three stages, which are used as quality gates. The first stage is `develop`, which holds all the non-tested features. After deskcheck, the app is promoted to `staging`, where the tests are done, and after that, the app is promoted to `production`, where it can be presented to stakeholders.

When a merge is done (through a pull request) to `main`, Heroku updates automatically the other pipeline, which then deploys to `production`. This other Heroku pipeline is responsable for the final app.

### Commits

Commits done in develop must follow the semantic-release pattern, just like below:

`git commit -m 'fix: CARD - your commit description'`
`git commit -m 'feat: CARD - your commit description'`

**OBS**: To other commands, check the [docs](https://github.com/semantic-release/semantic-release).

### Check-in dance

To do a check-in/commit, every developer must follow these steps:

Dictionary:
TYPE: Commit type, check Commits section.
CARD: Number/Description of the Trello card.

1. Run tests `pytest`
1. Commit to local
    1. Add files to staging `git add <fileName> -A` or `git add -p`
    1. Commit files `git commit -m "TYPE: CARD - your commit message"`
1. Check if the workflow in GitHub is green
1. Pull updates `git pull --rebase`
    1. Fix conflicted files
	    1. `git add <fixed files>`
	    1. `git rebase --continue`
    1. Run tests again `pytest`
1. Push your code `git push`
1. Check if the workflow in GitHub is green
    1. RED? Fix imediatelly or revert `git revert`

### How to collaborate?

To collaborate with the project, a developer can:

* If errors/improves are found, open a GitHub issue
* Open pull requests to `develop` branch.