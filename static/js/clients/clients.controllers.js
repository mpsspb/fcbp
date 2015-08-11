/**
* ClientsController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('ClientsController', ClientsController);

  ClientsController.$inject = ['$scope', '$http',
                               'Authentication', 'ClubCard', 'Clients'];

  /**
  * @namespace ClientsController
  */
  function ClientsController($scope, $http, Authentication, ClubCard, Clients) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();
    vm.clubcards = [];
    vm.clients = [];
    vm.previous_url = null;
    vm.next_url = null;
    vm.page = 1;
    
    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clients.controllers.ClientsController
    */
    function activate() {
      ClubCard.list().then(clubcardsSuccessFn, clubcardsErrorFn);

      /**
      * @name clubcardsSuccessFn
      * @desc Update ClubCard array on view
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

      Clients.list(vm.page).then(clientsSuccessFn, clientsErrorFn);

      /**
      * @name clientsSuccessFn
      * @desc Update Clients array on view
      */
      function clientsSuccessFn(data, status, headers, config) {
        vm.clients = data.data.results;
        vm.previous_url = data.data.previous;
        vm.next_url = data.data.next;
      }

      /**
      * @name clientsErrorFn
      * @desc console log error
      */
      function clientsErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };

    /**
    * @name ClientsPage
    * @desc update clients list for page
    * @memberOf fcbp.clients.controllers.ClientsController
    */
    vm.ClientsPage = function ClientsPage() {
      Clients.list(vm.page).then(clientsSuccessFn, clientsErrorFn);

      /**
      * @name clientsSuccessFn
      * @desc Update Clients array on view
      */
      function clientsSuccessFn(data, status, headers, config) {
        vm.clients = data.data.results;
        vm.previous_url = data.data.previous;
        vm.next_url = data.data.next;
      }

      /**
      * @name clientsErrorFn
      * @desc console log error
      */
      function clientsErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };

    /**
    * @name isAuthenticated
    * @desc Log the user out
    * @memberOf fcbp.clients.controllers.ClientsController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    };

  }
})();