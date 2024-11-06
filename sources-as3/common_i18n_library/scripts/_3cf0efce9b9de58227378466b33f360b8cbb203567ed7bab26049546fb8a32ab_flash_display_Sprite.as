package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _3cf0efce9b9de58227378466b33f360b8cbb203567ed7bab26049546fb8a32ab_flash_display_Sprite extends Sprite
   {
       
      
      public function _3cf0efce9b9de58227378466b33f360b8cbb203567ed7bab26049546fb8a32ab_flash_display_Sprite()
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
