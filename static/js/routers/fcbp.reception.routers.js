(function () {
  'use strict';

  angular
    .module('fcbp.reception.routes', ['ngRoute']);
    
  angular
    .module('fcbp.reception.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/reception', {
      controller: 'ReceptionController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/reception/reception.html'
    }).when('/online', {
      controller: 'OnlineController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/reception/online.html'
    })
  }
})();