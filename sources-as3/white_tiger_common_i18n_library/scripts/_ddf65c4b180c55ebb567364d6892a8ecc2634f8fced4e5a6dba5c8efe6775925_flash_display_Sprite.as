package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ddf65c4b180c55ebb567364d6892a8ecc2634f8fced4e5a6dba5c8efe6775925_flash_display_Sprite extends Sprite
   {
       
      
      public function _ddf65c4b180c55ebb567364d6892a8ecc2634f8fced4e5a6dba5c8efe6775925_flash_display_Sprite()
      {
         super();
      }
      
      public function allowDomainInRSL(... rest) : void
      {
         Security.allowDomain.apply(null,rest);
      }
      
      public function allowInsecureDomainInRSL(... rest) : void
      {
         Security.allowInsecureDomain.apply(null,rest);
      }
   }
}
