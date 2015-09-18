/**
* UseClientPersonalController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('UseClientPersonalController', UseClientPersonalController);

  UseClientPersonalController.$inject = ['$location', '$rootScope', '$routeParams', '$scope', 'Personals'];

  /**
  * @namespace UseClientPersonalController
  */
  function UseClientPersonalController($location, $rootScope, $routeParams, $scope, Personals) {
    var vm = this;

    vm.use = use;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clients.controllers.UseClientPersonalController
    */
    function activate() {

      var uid = $routeParams.uid
      Personals.get(uid).then(personalclientSuccessFn, personalclientErrorFn);

      /**
      * @name personalclientSuccessFn
      * @desc Update Personals array on view
      */
      function personalclientSuccessFn(data, status, headers, config) {
        vm.personal = data.data;
      }

      /**
      * @name personalclientErrorFn
      * @desc console log error
      */
      function personalclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    function use() {

      var uid = $routeParams.uid
      var fdata = {client_personal: uid}
      Personals.use(fdata).then(personalclientSuccessFn, personalclientErrorFn);

      /**
      * @name personalclientSuccessFn
      * @desc Update Personals array on view
      */
      function personalclientSuccessFn(data, status, headers, config) {
        activate();
        console.log('success')
      }

      /**
      * @name personalclientErrorFn
      * @desc console log error
      */
      function personalclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

  };

})();