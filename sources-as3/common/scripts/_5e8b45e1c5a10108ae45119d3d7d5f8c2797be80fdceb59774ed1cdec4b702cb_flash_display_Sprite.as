package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _5e8b45e1c5a10108ae45119d3d7d5f8c2797be80fdceb59774ed1cdec4b702cb_flash_display_Sprite extends Sprite
   {
       
      
      public function _5e8b45e1c5a10108ae45119d3d7d5f8c2797be80fdceb59774ed1cdec4b702cb_flash_display_Sprite()
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
