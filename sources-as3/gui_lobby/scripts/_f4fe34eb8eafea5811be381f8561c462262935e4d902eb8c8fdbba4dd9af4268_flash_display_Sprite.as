package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _f4fe34eb8eafea5811be381f8561c462262935e4d902eb8c8fdbba4dd9af4268_flash_display_Sprite extends Sprite
   {
       
      
      public function _f4fe34eb8eafea5811be381f8561c462262935e4d902eb8c8fdbba4dd9af4268_flash_display_Sprite()
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
