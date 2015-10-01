/**
* NewClientProductController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('NewClientProductController', NewClientProductController);

  NewClientProductController.$inject = ['$rootScope', '$routeParams', '$scope',
                                        '$http',
                                        'Clients', 'ClubCard', 'Timing',
                                        'AquaAerobics', 'Tickets', 'Personals',
                                        'ClientPayment'];

  /**
  * @namespace NewClientProductController
  */
  function NewClientProductController($rootScope, $routeParams, $scope, $http,
                                       Clients, ClubCard, Timing,
                                       AquaAerobics, Tickets, Personals,
                                       ClientPayment) {
    var vm = this;

    vm.submit = submit;
    vm.reset = reset;
    vm.chk_amount = chk_amount;
    vm.add_credit = add_credit;
    vm.remove_credit = remove_credit;
    vm.search_client = search_client;
    vm.add_client = add_client;
    vm.rm_client = rm_client;

    vm.fdata = {
      discount: 0,
      price: 0,
      payment_type: 1,
      is_credit: 0,
    };

    vm.extraclients = [];

    vm.credits = [];

    vm.clubcards = [];
    vm.aquaaerobicses = [];
    vm.tickets = [];
    vm.personals = [];
    vm.timings = [];

    vm.product_choose = product_choose;
    vm.total = total;

    activate();


    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clients.controllers.NewClientProductController
    */
    function activate() {

      var uid = $routeParams.uid
      Clients.get(uid).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update credit data on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        vm.client = data.data;
        vm.fdata.client = vm.client.id;
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

      ClubCard.list().then(clubcardsSuccessFn, clubcardsErrorFn);

      /**
      * @name clubcardsSuccessFn
      * @desc Update ClubCards array on view
      */
      function clubcardsSuccessFn(data, status, headers, config) {
        vm.clubcards = data.data;
      }

      /**
      * @name clubcardsErrorFn
      * @desc console log error
      */
      function clubcardsErrorFn(data, status, headers, config) {
        console.log(data);
      }

      AquaAerobics.list().then(aquaaerobicsesSuccessFn, aquaaerobicsesErrorFn);

      /**
      * @name aquaaerobicsesSuccessFn
      * @desc Update AquaAerobics array on view
      */
      function aquaaerobicsesSuccessFn(data, status, headers, config) {
        vm.aquaaerobicses = data.data;
      }

      /**
      * @name aquaaerobicsesErrorFn
      * @desc console log error
      */
      function aquaaerobicsesErrorFn(data, status, headers, config) {
        console.log(data);
      }

      Tickets.list().then(ticketsSuccessFn, ticketsErrorFn);

      /**
      * @name ticketsSuccessFn
      * @desc Update Tickets array on view
      */
      function ticketsSuccessFn(data, status, headers, config) {
        vm.tickets = data.data;
      }

      /**
      * @name ticketsErrorFn
      * @desc console log error
      */
      function ticketsErrorFn(data, status, headers, config) {
        console.log(data);
      }

      Personals.list().then(personalsSuccessFn, personalsErrorFn);

      /**
      * @name personalsSuccessFn
      * @desc Update Personal array on view
      */
      function personalsSuccessFn(data, status, headers, config) {
        vm.personals = data.data;
      }

      /**
      * @name personalsErrorFn
      * @desc console log error
      */
      function personalsErrorFn(data, status, headers, config) {
        console.log(data);
      }

      Timing.list().then(timingsSuccessFn, timingsErrorFn);

      /**
      * @name timingsSuccessFn
      * @desc Update Timing array on view
      */
      function timingsSuccessFn(data, status, headers, config) {
        vm.timings = data.data;
      }

      /**
      * @name timingsErrorFn
      * @desc console log error
      */
      function timingsErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    $scope.$watch('vm.fdata.product', function(id){
      angular.forEach(vm.options, function(attr){
        if(attr.id === id){
          vm.fdata.price = attr.price;
          vm.fdata.amount = vm.total();
          vm.fdata.clients_count = attr.clients_count;
        }
      });
    });

    $scope.$watch('vm.fdata.discount', function(id){
          vm.fdata.amount = vm.total();
    });

    /**
    * @name submit
    * @desc Create a new Client Product
    * @memberOf fcbp.client.controllers.NewClientProductController
    */
    function submit() {

      if (vm.chk_amount() != 0 && !vm.fdata.is_credit){
        console.log('error amount')
        return 0;
      }

      if ( vm.fdata.is_credit ) {
        var d = new Date();
        var day = d.getDate();
        var month = d.getMonth() + 1;
        var year = d.getFullYear();
        var credit_date = day + '.' + month + '.' + year
        vm.credits.push({'amount': vm.chk_amount(),
                       'date': credit_date});
      }

      vm.fdata.credits = vm.credits;

      if (vm.product == 'card') {
        vm.fdata.club_card = vm.fdata.product
        $http.post('/api/v1/clients/clubcard/', vm.fdata)
             .then(SuccessFn, ErrorFn);
      } else if (vm.product == 'aqua') {
        vm.fdata.aqua_aerobics = vm.fdata.product
        $http.post('/api/v1/clients/aquaaerobics/', vm.fdata)
             .then(SuccessFn, ErrorFn);
      } else if (vm.product == 'ticket') {
        vm.fdata.ticket = vm.fdata.product
        $http.post('/api/v1/clients/ticket/', vm.fdata)
             .then(SuccessFn, ErrorFn);
      } else if (vm.product == 'personal') {
        vm.fdata.personal = vm.fdata.product
        $http.post('/api/v1/clients/personal/', vm.fdata)
             .then(SuccessFn, ErrorFn);
      } else if (vm.product == 'timing') {
        vm.fdata.timing = vm.fdata.product
        $http.post('/api/v1/clients/timing/', vm.fdata)
             .then(SuccessFn, ErrorFn);
      } else {
        console.log('error product');
        return 0;
      }

      if (!vm.fdata.product) {
        console.log('error choose product');
        return 0;
      }

      /**
      * @name createClientPayment
      * @desc Propogate error event and show snackbar with error message
      */
      function SuccessFn(data, status, headers, config) {
        if ( data['status'] == 201 ){
          console.log('Success! ClientPayment created.');
          window.location = '/#/cardclient/' + vm.client.id + '/';
        } else {
          console.log(data)
          $rootScope.$broadcast('ClientPayment.created.error');
        }
      }

      function ErrorFn(data, status, headers, config) {
          console.log(data)
          $rootScope.$broadcast('ClientPayment.created.error');
      }

    };

    /**
    * @name product_choose
    * @desc Return current choose of the product type
    * @memberOf fcbp.client.controllers.NewClientProductController
    */
    function product_choose(name){
      if (vm.product == 'card') {
        return 'Клубная карта'
      } else if (vm.product == 'aqua') {
        return 'Аквааэробика'
      } else if (vm.product == 'ticket') {
        return 'Абонемент'
      } else if (vm.product == 'personal') {
        return 'Персональные тренировки'
      } else if (vm.product == 'timing') {
        return 'С учетом времени'
      } else {
        return 'Ничего не выбрано'
      }
    }

    /**
    * @name total
    * @desc Return current total sum for pay
    * @memberOf fcbp.client.controllers.NewClientProductController
    */
    function total() {
      var total = vm.fdata.price * (100 - vm.fdata.discount) / 100;
      return total;
    }

    /**
    * @name chk_amount
    * @desc Return is correct the sum of all payments
    * @memberOf fcbp.client.controllers.NewClientProductController
    */
    function chk_amount() {
      var total = vm.total();
      var payments = vm.fdata.amount;
      vm.credits.forEach(function(credit) {
          payments += credit.amount;
      });
      return (total - payments);
    }

    /**
    * @name reset
    * @desc Reset pay
    * @memberOf fcbp.client.controllers.NewClientProductController
    */
    function reset () {
      vm.fdata.price = 0;
      vm.fdata.product = '';
      vm.fdata.amount = 0;
      vm.fdata.discount = 0;
      vm.fdata.clients_count = 0;
      vm.total();
      vm.credits = [];
      vm.extraclients = [];
    }

    /**
    * @name add_credit
    * @desc add_credit pay
    * @memberOf fcbp.client.controllers.NewClientProductController
    */
    function add_credit () {
      var msg = "";

      var day = vm.credit_date.split('.')[0]

      if (day < 1 || day > 31) {
        msg = "День должен быть в диапазоне от 1 до 31.";
        console.log(msg);
        return 101;
      }

      var month = vm.credit_date.split('.')[1]
      var year = '20' + vm.credit_date.split('.')[2]

      if (month < 1 || month > 12) { // check month range
        msg = "Месяц должен быть в диапазоне от 1 до 12.";
        console.log(msg);
        return 101;
      }

      if (month == 2) { // check for february 29th
        var isleap = (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0));
        if (day>29 || (day==29 && !isleap)) {
            msg = "В феврале " + year + " не " + day + " дней!";
            console.log(msg);
            return 102;
        }
      }

      var credit_date = day + '.' + month + '.' + year; //25.10.2006

      vm.credits.push({'amount': vm.credit_amount,
                       'date': credit_date});
      vm.credit_amount = '';
      vm.credit_date = '';
    }

    /**
    * @name remove_credit
    * @desc remove_credit pay
    * @memberOf fcbp.client.controllers.NewClientProductController
    */
    function remove_credit (key){
          vm.credits.splice(key, 1);
    }

    /* Search external clients if vm.clients_count > 1
    */
    function search_client() {
      Clients.full_search(vm.ext).then(clntSearchSuccessFn, clntSearchErrorFn);

      function clntSearchSuccessFn(data, status, headers, config) {
        if (data.data.length == 1) {
          var clnt = data.data[0]
          var born = clnt.born.split('-')
          born = born[2] + '.' + born[1] + '.' + born[0].substring(2,4)
          vm.ext = {
            last_name: clnt.last_name,
            first_name: clnt.first_name,
            patronymic: clnt.patronymic,
            born: born,
            id: -1
          }
        } else {
          vm.findClients = data.data;
        }
      }

      function clntSearchErrorFn(data, status, headers, config) {
        console.log(data);
      }
    }

    /*
    * Create or add clients to the external array.
    */
    function add_client(key) {
      if ( key < 0) {
        vm.ext.full_name = vm.ext.last_name + ' ' + vm.ext.first_name + ' ' + vm.ext.patronymic
        vm.extraclients.push(vm.ext)
      } else {
        vm.extraclients.push(vm.findClients[key]);        
      }
      vm.findClients = [];
      vm.ext = {};
    }

    /*
    * Create or add clients to the external array.
    */
    function rm_client(key) {
      vm.extraclients.splice(key, 1);
      vm.findClients = [];
      vm.ext = {};
    }

  };

  

})();