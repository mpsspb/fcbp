/**
* UseClientTicketController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('UseClientTicketController', UseClientTicketController);

  UseClientTicketController.$inject = ['$location', '$rootScope', '$routeParams', '$scope', 'Tickets'];

  /**
  * @namespace UseClientTicketController
  */
  function UseClientTicketController($location, $rootScope, $routeParams, $scope, Tickets) {
    var vm = this;

    vm.use = use;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clients.controllers.UseClientTicketController
    */
    function activate() {

      var uid = $routeParams.uid
      Tickets.get(uid).then(aquaclientSuccessFn, aquaclientErrorFn);

      /**
      * @name aquaclientSuccessFn
      * @desc Update Tickets array on view
      */
      function aquaclientSuccessFn(data, status, headers, config) {
        vm.ticket = data.data;
      }

      /**
      * @name aquaclientErrorFn
      * @desc console log error
      */
      function aquaclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    function use() {

      var uid = $routeParams.uid
      var fdata = {client_ticket: uid}
      Tickets.use(fdata).then(aquaclientSuccessFn, aquaclientErrorFn);

      /**
      * @name aquaclientSuccessFn
      * @desc Update Tickets array on view
      */
      function aquaclientSuccessFn(data, status, headers, config) {
        activate();
        console.log('success')
      }

      /**
      * @name aquaclientErrorFn
      * @desc console log error
      */
      function aquaclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

  };

})();