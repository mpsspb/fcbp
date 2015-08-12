/**
* ProductsController
* @namespace fcbp.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.layout.controllers')
    .controller('ProductsController', ProductsController);

  ProductsController.$inject = ['$scope', '$http', 'Authentication' ];

  /**
  * @namespace ProductsController
  */
  function ProductsController($scope, $http, Authentication ) {
    var vm = this;

    vm.isAuthenticated = isAuthenticated();

    /**
    * @name isAuthenticated
    * @desc Log the user out
    * @memberOf fcbp.layout.controllers.ProductsController
    */
    function isAuthenticated() {
      return Authentication.isAuthenticated();
    };

  }
})();