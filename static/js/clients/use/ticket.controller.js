/**
* UseClientTicketController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('UseClientTicketController', UseClientTicketController);

  UseClientTicketController.$inject = ['$location', '$rootScope', '$routeParams', '$scope',
                                       '$http', 'ClientPayment', 'Tickets'];

  /**
  * @namespace UseClientTicketController
  */
  function UseClientTicketController($location, $rootScope, $routeParams, $scope, $http,
                                     ClientPayment, Tickets) {
    var vm = this;

    vm.uid = $routeParams.uid;
    vm.use = use;
    vm.freeze = freeze;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clients.controllers.UseClientTicketController
    */
    function activate() {

      // freeze data
      vm.frdata = {
        days: 1,
        amount: 0.0,
        is_paid: false,
        client_aqua: vm.uid,
        fdate: moment().format('DD.MM.YYYY'),
        is_credit: false
      };

      Tickets.get(vm.uid).then(ticketclientSuccessFn, ticketclientErrorFn);

      /**
      * @name ticketclientSuccessFn
      * @desc Update Tickets array on view
      */
      function ticketclientSuccessFn(data, status, headers, config) {
        vm.ticket = data.data;
      }

      /**
      * @name ticketclientErrorFn
      * @desc console log error
      */
      function ticketclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    function use() {

      var fdata = {client_ticket: vm.uid}
      Tickets.use(fdata).then(ticketclientSuccessFn, ticketclientErrorFn);

      /**
      * @name ticketclientSuccessFn
      * @desc Update Tickets array on view
      */
      function ticketclientSuccessFn(data, status, headers, config) {
        activate();
        console.log('success')
      }

      /**
      * @name ticketclientErrorFn
      * @desc console log error
      */
      function ticketclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };

    function freeze() {

      if ( vm.frdata.is_credit ) {
        var credit_date = moment().add(1, 'days').startOf('day').format('DD.MM.YYYY');
        vm.frdata.schedule = credit_date;
        vm.frdata.discount = 0;
        vm.frdata.count = 1;
      }

      Tickets.freeze(vm.uid, vm.frdata).then(freezeSuccessFn, freezeErrorFn);

      /**
      * @name freezeSuccessFn
      * @desc Update Tickets array on view
      */
      function freezeSuccessFn(data, status, headers, config) {
        console.log(data);
        activate();
      }

      /**
      * @name freezeErrorFn
      * @desc console log error
      */
      function freezeErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };

  };

})();