(function () {
  'use strict';

  angular
    .module('fcbp.auth', [
      'fcbp.auth.controllers',
      'fcbp.auth.services'
    ]);

  angular
    .module('fcbp.auth.controllers', []);

  angular
    .module('fcbp.auth.services', ['ngCookies']);
})();