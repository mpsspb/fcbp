/**
* PersonalsController
* @namespace fcbp.personals.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.personals.controllers')
    .controller('PersonalsController', PersonalsController);

  PersonalsController.$inject = ['$scope', '$http', 'Authentication', 'Personals'];

  /**
  * @namespace PersonalsController
  */
  function PersonalsController($scope, $http, Authentication, Personals) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();
    vm.personals = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.personals.controllers.PersonalsController
    */
    function activate() {

      Personals.list().then(personalsSuccessFn, personalsErrorFn);

      $scope.$on('personal.created', function (event, personal) {
        Personals.list().then(personalsSuccessFn, personalsErrorFn);
      });

      $scope.$on('personal.created.error', function () {
        // vm.personals.shift();
      });

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

    };

    /**
    * @name isAuthenticated
    * @desc Log the user out
    * @memberOf fcbp.personals.controllers.PersonalsController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    };

  }
})();