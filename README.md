# Academy_TOP_BolshakovVV_13_2
# Задание 1
На занятии вы видели как мною были написаны 3 эхо
сервера и клиенты для них:
- простой (1-запрос, 1-ответ);
- расширенный (сколько хочешь запросов всегда
отвечает) но в текущий момент может работать
только с одним клиентом;
- многопоточный - то же что и расширенный но
параллельно может работать с несколькими
клиентами.

Ваше задание будет модифицировать расширенный и
многопоточный сервера таким образом чтобы
улучшить их стабильность и расширить возможность
взаимодействия с ними. Какие проблемы вам надо
решить (я их специально показал на уроке)
- добавить возможность отключения клиента если он
ввел нужную команду;
- решить проблему с тем что сервер падает в цикл
при отключении клиента;
- решить проблему зависания как сервера так и
клиента если клиент вместо того чтобы ввести
сообщение просто нажал ввод;
- дать возможность по команде клиента выключить
сервер, при этом клиент продолжает работу. Далее
клиент отправляет отключенному серверу какоенибудь сообщение, клиент не выпадает с ошибкой, а
выдает сообщение о разрыве подключение и
завершает работу с сообщением: “Process finished
with exit code 0” пример на странице ниже.

```
Type the message to send: stop server
Received:
Type the messege to send: asd
Програма на вашем хост-компьютере разорвала установленное подключение

Process finished with exit code 0
```