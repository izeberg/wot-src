package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _d649172ed1a9e5ab3e0381a49096e4cce137ad2238ebd769d89be8521e08189d_flash_display_Sprite extends Sprite
   {
       
      
      public function _d649172ed1a9e5ab3e0381a49096e4cce137ad2238ebd769d89be8521e08189d_flash_display_Sprite()
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
