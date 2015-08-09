/**
* ClientsController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('ClientsController', ClientsController);

  ClientsController.$inject = ['$scope', '$http', 'Authentication', 'ClubCard'];

  /**
  * @namespace ClientsController
  */
  function ClientsController($scope, $http, Authentication, ClubCard) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();
    vm.clubcards = [];

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