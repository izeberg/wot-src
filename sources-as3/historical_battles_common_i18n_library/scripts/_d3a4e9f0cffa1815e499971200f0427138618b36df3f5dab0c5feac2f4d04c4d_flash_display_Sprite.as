package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _d3a4e9f0cffa1815e499971200f0427138618b36df3f5dab0c5feac2f4d04c4d_flash_display_Sprite extends Sprite
   {
       
      
      public function _d3a4e9f0cffa1815e499971200f0427138618b36df3f5dab0c5feac2f4d04c4d_flash_display_Sprite()
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
